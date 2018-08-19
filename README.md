![alt text](https://i.imgur.com/yztjtDY.png "Logo Title Text 1")

## Processing Images Bot for Reddit /r/processingimages `V1.3.0`

#### This bot uses the Processing language to take a randomly selected image from any subreddit on Reddit.com and alters it.

#### Some premade sketches will be used from https://www.openprocessing.org/ please check it out.

Using the Processing.py Java compiler I am writing processing code in python.
Check out the subreddit:

https://reddit.com/r/processingimages
<br/>

### `Config.yml` If you wish to use this bot here is the configuration.
```yaml
processing.config:
  processing.path:
    sketches:  #List of templates
      - "template_circle"
      - "template_letters"
      - "template_line"


  bot.config:
    reddit_subreddit: "art" #subreddit to pick random submissions from


  imgur.config:
    imgur_client_id: ""
    imgur_app_secret: ""
    imgur_access_token: "" #Not required if you're using pyimgur

  reddit.config:
    reddit_app_username: ""  #In order to make submissions a username is required
    reddit_app_password: ""   #In order to make submissions a password is required
    reddit_client_id: ""  
    reddit_app_secret: ""
```

---

### How the naming system works:
### `< randomly generated ID >+< subreddit name >`
#### Ex: `< QWCUF7W9 >< art >`

---

### `V1.0.1` Changes:
`-- Bot now post original Image Imgur link as comment`

### `V1.0.2` Changes:
`-- Bot now has a config function to sleep for x seconds`

### `V1.1.0` Changes:
`-- Bot now has different processing templates to choose from randomly`

### `V1.2.1` Changes:
`-- Bot now stores all the retrieved urls for future reference`

### `V1.2.9` Changes:
`-- Added a new template to the random picker`

`-- Fixed a bug where Java ran out of memory too quickly`

`-- Fixed a bug where .png images would be chosen when .jpg images should be chosen`

`-- Removed while loop in favor of cron`

## `V1.3.0` Changes:

`-- Bot now picks randomly from different subreddits. A list of subreddit can be found in subredditlist.txt`

`-- Bug fixes and optimizations`
