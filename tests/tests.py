#This will be filled with test cases soon
import unittest
import yaml
from redditpy import redditpy
import re

with open("config.yml", "r") as configFile:
    config = yaml.load(configFile)
imgur_client_id = config["processing.config"]["imgur.config"]["imgur_client_id"]
imgur_app_secret = config["processing.config"]["imgur.config"]["imgur_app_secret"]
reddit_client_id = config["processing.config"]["reddit.config"]["reddit_client_id"]
reddit_app_secret = config["processing.config"]["reddit.config"]["reddit_app_secret"]
reddit_app_username = config["processing.config"]["reddit.config"]["reddit_app_username"]
reddit_app_password = config["processing.config"]["reddit.config"]["reddit_app_password"]
sleep_interval = config["processing.config"]["bot.config"]["interval-seconds"]


r = redditpy.Reddit(
username=reddit_app_username,
password=reddit_app_password,
subreddit="pics",
app_id=reddit_client_id,
app_secret=reddit_app_secret,
pimg_id=imgur_client_id,
pimg_secret=imgur_app_secret)

class RedditPyTest(unittest.TestCase):
    def test_get_url(self):
        random_submission = r.get_random_submission()
        HttpsMatch = re.findall(r"(?:http|ftp)s?:\/\/", random_submission)
        self.assertEqual(len(HttpsMatch), 1)

    def test_post_imgur(self):
        image_url = str(r.upload_imgur("./media/preprocessed/test.jpg").link)
        HttpsMatch = re.findall(r"(?:http|ftp)s?:\/\/", image_url)
        self.assertEqual(len(HttpsMatch), 1)

    def test_post_reddit(self):
        post_reddit_test = r.post_image("https://i.imgur.com/VAPyjGZ.jpg", mock=True)
        self.assertEqual(post_reddit_test, None)

    def test_download_url(self):
        download = r.download_url("https://i.imgur.com/VAPyjGZ.jpg")
        self.assertEqual(1, 1)

    def test_download_url_nonimgur(self):
        download_non_imgur = r.download_url("https://www.cytonix.com/v/vspfiles/photos/homepage/1525876425644.jpg")
        self.assertEqual(1, 1)
