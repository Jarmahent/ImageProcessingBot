from redditpy import redditpy
import yaml
import sys
from colorama import Fore, Style
from colorama import init as colorinit
import random
from bot_db.connection import DbConnection
from processing_handler.processing_handler import P5
class RedditBot:
    def __init__(self, subreddit):
        with open("config.yml", "r") as ymlconfig:
            config = yaml.load(ymlconfig)

        imgur_client_id = config["processing.config"]["imgur.config"]["imgur_client_id"]
        imgur_app_secret = config["processing.config"]["imgur.config"]["imgur_app_secret"]
        reddit_client_id = config["processing.config"]["reddit.config"]["reddit_client_id"]
        reddit_app_secret = config["processing.config"]["reddit.config"]["reddit_app_secret"]
        reddit_app_username = config["processing.config"]["reddit.config"]["reddit_app_username"]
        reddit_app_password = config["processing.config"]["reddit.config"]["reddit_app_password"]

        self._processing_templates = config["processing.config"]["processing.path"]["sketches"]

        self._redditClass = redditpy.Reddit(
        username=reddit_app_username,
        password=reddit_app_password,
        app_id=reddit_client_id,
        app_secret=reddit_app_secret,
        subreddit=subreddit,
        pimg_id=imgur_client_id,
        pimg_secret=imgur_app_secret)

        self._checker = DbConnection()
        colorinit(convert=False)
    def run(self):
        try:
            print(f"{Fore.RED}Starting...!{Style.RESET_ALL}")

            #Retrieve A random Submission from the subreddit
            random_submission_url = self._redditClass.get_random_submission()

            #If the URL is already in the DB then return None and let the while
            # loop start the function again
            if self._checker.urlIsDupe(random_submission_url) == True:
                print(f"{Fore.RED}URL has already been used exiting..{Style.RESET_ALL}")
                sys.exit("Duplicate URL")
                return None

            #Add url to sqlite3 db ~ bot.db ~
            print(f"{Fore.GREEN} Adding Url To Database {Style.RESET_ALL}")
            self._checker.insert_url(random_submission_url)
            print(f"{Fore.GREEN}URL Added..!{Style.RESET_ALL}")


            #print(random_submission_url)
            print(f"{Fore.GREEN}Getting random url...{Style.RESET_ALL}")



            #Download that submission into /media/preprocessed
            print(f"{Fore.GREEN}Downloading to {Fore.RED}/media/preprocessed{Style.RESET_ALL}")
            preprocessed_download = self._redditClass.download_url(random_submission_url)


            #Process that Image using processing ~Todo: pick a random sketch to process with...~
            #Push processed image into /media/processed folder
            #Pick a random template
            sketch = P5()
            print(f"{Fore.GREEN}Running sketch...{Style.RESET_ALL}")
            random_template = random.choice(self._processing_templates)
            print(f"{Fore.GREEN}Picking random template{Style.RESET_ALL}")
            print(f"{Fore.GREEN}Template picked is: {Fore.RED}{random_template}{Style.RESET_ALL}")
            sketch.run_sketch(random_template)
            print(f"{Fore.GREEN}Sketch made!{Style.RESET_ALL}")

            #Upload Image to Imgur   MIGHT CHANGE SOON BECUASE COMPRESSION ISSUES
            #Change preprocessed to processed once the processing stage is complete
            print(f"{Fore.GREEN}Uploading to imgur{Style.RESET_ALL}")
            upload_to_imgur = self._redditClass.upload_imgur(image_path="./media/processed/processed.png")


            #Post processed image to /r/processingimages
            print(f"{Fore.GREEN}Posting to Reddit...{Style.RESET_ALL}")
            post_to_reddit = self._redditClass.post_image(upload_to_imgur.link)
            print(f"{Fore.GREEN}ID: {Fore.RED}{post_to_reddit}{Style.RESET_ALL}")
            print(f"{Fore.GREEN}URL: {Fore.RED}https://www.reddit.com/r/processingimages/comments/{post_to_reddit}{Style.RESET_ALL}")

            #Post a comment on the new Submission with the link to the original image
            comment_info = self._redditClass.comment_info(id=str(post_to_reddit), data=f"Original Image: {random_submission_url}")


            return post_to_reddit
        except Exception as e:
            return e





if __name__ == "__main__":
    with open("config.yml", "r") as subredditconf:
        sconfig = yaml.load(subredditconf)
    subreddits = sconfig["processing.config"]["bot.config"]["reddit_subreddit"]
    random_subreddit = random.choice(subreddits)
    print(f"Picking random Image from {random_subreddit}")
    bot = RedditBot(random_subreddit)
    bot.run()
