from redditpy import redditpy
import yaml
from processing_handler.processing_handler import P5
class RedditBot:
    def __init__(self):
        with open("config.yml", "r") as ymlconfig:
            config = yaml.load(ymlconfig)

        imgur_client_id = config["processing.config"]["imgur.config"]["imgur_client_id"]
        imgur_app_secret = config["processing.config"]["imgur.config"]["imgur_app_secret"]
        reddit_client_id = config["processing.config"]["reddit.config"]["reddit_client_id"]
        reddit_app_secret = config["processing.config"]["reddit.config"]["reddit_app_secret"]
        reddit_app_username = config["processing.config"]["reddit.config"]["reddit_app_username"]
        reddit_app_password = config["processing.config"]["reddit.config"]["reddit_app_password"]
        subreddit = config["processing.config"]["bot.config"]["reddit_subreddit"]
        self._sleep_interval = config["processing.config"]["bot.config"]["interval-seconds"]
        self._loop_boolean = config["processing.config"]["bot.config"]["loop"]

        self._redditClass = redditpy.Reddit(
        username=reddit_app_username,
        password=reddit_app_password,
        app_id=reddit_client_id,
        app_secret=reddit_app_secret,
        subreddit=subreddit,
        pimg_id=imgur_client_id,
        pimg_secret=imgur_app_secret)

    def run(self):
        try:
            #Retrieve A random Submission from the subreddit
            random_submission_url = self._redditClass.get_random_submission()
            #print(random_submission_url)
            print("Getting random url...")



            #Download that submission into /media/preprocessed
            print("Downloading to /media/preprocessed")
            preprocessed_download = self._redditClass.download_url(random_submission_url)
            print(preprocessed_download)


            #Process that Image using processing ~Todo: pick a random sketch to process with...~
            #Push processed image into /media/processed folder
            sketch = P5()
            print("Running sketch...")
            sketch.run_sketch("template_circle")


            #Upload Image to Imgur
            #Change preprocessed to processed once the processing stage is complete
            upload_to_imgur = self._redditClass.upload_imgur(image_path="./media/processed/processed.png")
            print("Uploading to imgur")

            #Post processed image to /r/processingimages
            print("Posting to Reddit...")
            post_to_reddit = self._redditClass.post_image(upload_to_imgur.link)
            print(post_to_reddit)

            #Post a comment on the new Submission with the link to the original image
            comment_info = self._redditClass.comment_info(id=str(post_to_reddit), data=f"Original Image: {random_submission_url}")

            #Sleep for x seconds
            if self._loop_boolean == True:
                self._redditClass.sleep(self._sleep_interval)

            return post_to_reddit
        except Exception as e:
            return e





if __name__ == "__main__":
    bot = RedditBot()
    with open("config.yml", "r") as ymlconfig:
        loop = yaml.load(ymlconfig)
    loop_boolean = loop["processing.config"]["bot.config"]["loop"]
    while True:
        bot.run()
        if loop_boolean == False: break
