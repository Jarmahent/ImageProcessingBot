#This will be filled with test cases soon
import unittest
import yaml
from redditpy import redditpy
import re

with open("config.yml", "r") as configFile:
    config = yaml.load(configFile)
imgur_client_id = config["proccesing.config"]["imgur.config"]["imgur_client_id"]
imgur_app_secret = config["proccesing.config"]["imgur.config"]["imgur_app_secret"]
reddit_client_id = config["proccesing.config"]["reddit.config"]["reddit_client_id"]
reddit_app_secret = config["proccesing.config"]["reddit.config"]["reddit_app_secret"]

r = redditpy.Reddit(
subreddit="pics",
app_id=reddit_client_id,
app_secret=reddit_app_secret,
pimg_id=imgur_client_id,
pimg_secret=imgur_app_secret)

class RedditPyTest(unittest.TestCase):
    def test_get_url(self):
        random_submission = r.get_random_submission()
        HttpsMatch = re.findall(r"(?:http|ftp)s?:\/\/", random_submission)
        self.assertEquals(len(HttpsMatch), 1)

    def test_post_imgur(self):
        image_url = str(r.upload_imgur("./media/preprocessed/test.jpg").link)
        print(image_url)
        HttpsMatch = re.findall(r"(?:http|ftp)s?:\/\/", image_url)
        self.assertEquals(len(HttpsMatch), 1)
