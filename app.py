from redditpy import redditpy
import yaml
#Testing phase
with open("config.yml", "r") as ymlconfig:
    config = yaml.load(ymlconfig)

imgur_client_id = config["proccesing.config"]["imgur.config"]["imgur_client_id"]
imgur_app_secret = config["proccesing.config"]["imgur.config"]["imgur_app_secret"]
reddit_client_id = config["proccesing.config"]["reddit.config"]["reddit_client_id"]
reddit_app_secret = config["proccesing.config"]["reddit.config"]["reddit_app_secret"]
reddit_app_username = config["proccesing.config"]["reddit.config"]["reddit_app_username"]
reddit_app_password = config["proccesing.config"]["reddit.config"]["reddit_app_password"]

r = redditpy.Reddit(
username=reddit_app_username,
password=reddit_app_password,
app_id=reddit_client_id,
app_secret=reddit_app_secret,
subreddit="pics",
pimg_id=imgur_client_id,
pimg_secret=imgur_app_secret)
post = r.post_image("https://i.imgur.com/VAPyjGZ.jpg")
print(post)
