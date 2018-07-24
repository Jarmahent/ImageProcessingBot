from redditpy import redditpy
import yaml

class RedditBot:
    def __init__(self):
        with open("config.yml", "r") as ymlconfig:
            config = yaml.load(ymlconfig)

        imgur_client_id = config["proccesing.config"]["imgur.config"]["imgur_client_id"]
        imgur_app_secret = config["proccesing.config"]["imgur.config"]["imgur_app_secret"]
        reddit_client_id = config["proccesing.config"]["reddit.config"]["reddit_client_id"]
        reddit_app_secret = config["proccesing.config"]["reddit.config"]["reddit_app_secret"]
        reddit_app_username = config["proccesing.config"]["reddit.config"]["reddit_app_username"]
        reddit_app_password = config["proccesing.config"]["reddit.config"]["reddit_app_password"]

        self._redditClass = redditpy.Reddit(
        username=reddit_app_username,
        password=reddit_app_password,
        app_id=reddit_client_id,
        app_secret=reddit_app_secret,
        subreddit="pics",
        pimg_id=imgur_client_id,
        pimg_secret=imgur_app_secret)

    def run(self):
        try:
            #Retrieve A random Submission from the subreddit
            random_submission_url = self._redditClass.get_random_submission()
            print("Getting random url...")



            #Download that submission into /media/preprocessed
            print("Downloading to /media/preprocessed")
            preprocessed_download = self._redditClass.download_url(random_submission_url)
            #Process that Image using processing ~Todo: pick a random sketch to process with...~
            #Push processed image into /media/processed folder



            #Upload Image to Imgur
            upload_to_imgur = self._redditClass.upload_imgur(image_path="./media/processed/test.jpg")
            print("Uploading to imgur")

            #Post processed image to /r/processingimages
            print("Posting to Reddit...")
            post_to_reddit = self._redditClass.post_image(upload_to_imgur.link)

            return post_to_reddit
        except Exception as e:
            return e





if __name__ == "__main__":
    bot = RedditBot()
    bot.run()
