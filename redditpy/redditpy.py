from praw import Reddit as PrawReddit
import os
import sys
import string
import random
import time
from random import randint
from urllib import request
import pyimgur

class Reddit():
    def __init__(self, **kwargs):
        self._subreddit = kwargs["subreddit"]

        self._reddit = PrawReddit(
            username=kwargs["username"],
            password=kwargs["password"],
            client_id=kwargs["app_id"],
            client_secret=kwargs["app_secret"],
            user_agent="Reddit processing bot"
        )
        self._pimg = pyimgur.Imgur(
            client_id = kwargs["pimg_id"],
            client_secret = kwargs["pimg_secret"]
        )

    def generate_name(self, size=randint(3, 10), chars=string.ascii_uppercase + string.digits):  # Create a random name
        return ''.join(random.choice(chars) for _ in range(size))

    def get_random_submission(self):
        #Get a random submission from the selected subreddit
        try:
            return self._reddit.subreddit(self._subreddit).random().url
        except Exception as e:
            return e

    def download_url(self, url):

        if ".jpg" in url:
            download = request.urlretrieve(url, "media/preprocessed/preprocessed.jpg")
            print(f" {url} \n JPG format ")
            return download
        else:
            sys.exit(f"URL did not have .jpg as extension \n {url}")

    def sleep(self, seconds=None):
        try:
            print(f'Sleeping for {seconds} second(s)')
            for seconds_time in range(1, seconds +1):
                print(".", end="", flush=True)
                time.sleep(1)
            return None
        except Exception as e:
            return e

    def post_image(self, url, mock=False):
        '''
        Post image from url to reddit.com/r/processingimages
        Set Mock to True for testing...
        '''
        if mock == True:
            try:
                post_to_reddit = self._reddit.subreddit("processingimages").submit(
                title=self.generate_name(),
                url=url)
                print("Created submission...")
                delete_post = self._reddit.submission(id=str(post_to_reddit)).delete()
                print("Deleted Submission... \n Mock=True")
                return delete_post
            except Exception as e:
                return e
        else:
            try:
                post_to_reddit = self._reddit.subreddit("processingimages").submit(
                title=self.generate_name()+self._subreddit,
                url=url)
                return post_to_reddit
            except Except as e:
                return e


    def upload_imgur(self, image_path=None):
        #Upload image to Imgur
        try:
            image_upload = self._pimg.upload_image(image_path, title=self.generate_name())
            return image_upload
        except Exception as e:
            sys.exit(e)

    def comment_info(self, id=None, data=None):
        try:
            submission = self._reddit.submission(id=id).reply(data)
            return submission
        except Exception as e:
            return e
