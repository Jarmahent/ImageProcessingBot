from praw import Reddit as PrawReddit
import os
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
        self._localDirectory = os.path.expanduser("~")
        if not os.path.exists(os.path.join(self._localDirectory, "Pictures", "PyPics")):
            os.makedirs(os.path.join(self._localDirectory, "Pictures", "PyPics"))
            print("Creating Path for pictures... \n Path created in Pictures directory")


    def generate_name(self, size=randint(3, 10), chars=string.ascii_uppercase + string.digits):  # Create a random name
        return ''.join(random.choice(chars) for _ in range(size))

    def get_random_submission(self):
        #Get a random submission from the selected subreddit
        try:
            return self._reddit.subreddit(self._subreddit).random()
        except Exception as e:
            return e

    def download_url(self, url):
        #Download from url and place in pypics directory inside Pictures/
        if not ".jpg" in url and "imgur" in url:
            imgur_url = url.split('/')[-1].split('.')[0]

            print(imgur_url)

            self._pimg.get_image(id=imgur_url).download(
            path=os.path.join(self._localDirectory, "Pictures", "PyPics"),
            name=self.generate_name(),
            overwrite=False,
            size=None)

            print("Base Imgur URL")
        if ".jpg" in url:
            request.urlretrieve(url, os.path.join(self._localDirectory, "Pictures", "PyPics") + "{}{}{}".format("\\", self.generate_name(), ".jpg"))
            print(" JPG format ")

    def sleep(self, seconds):
        print(f'Sleeping for {seconds} second(s)')
        for seconds_time in range(1, seconds +1):
            print(".", end="", flush=True)
            time.sleep(1)
        return None

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
                title=self.generate_name(),
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
            return e
