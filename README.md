![alt text](https://i.imgur.com/yztjtDY.png "Logo Title Text 1")

## Processing Images Bot for Reddit /r/processingimages `V1.0.2`

#### This bot uses the Processing language to take an a randomly selected image from any subreddit on Reddit.com and alters it.

#### Some premade sketches will be used from https://www.openprocessing.org/ please check it out.

Using the Processing.py Java compiler I am writing processing code in python.

### `Config.yml` If you wish to use this bot here is the configuration.
```yaml
processing.config:
  processing.path:
    java.path: ''   #Not implemented yet
    sketch.path: ''  #Not implmented yet

  bot.config:
    loop: True #Run bot to loop once or not
    reddit_subreddit: "art" #subreddit to pick random submissions from
    interval-seconds: 30  #Loop interval for bot


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


How the naming system works:
< randomly generated ID >+< subreddit name >

Ex: < QWCUF7W9 >< art >

#### `V1.0.1` Changes:
`-- Bot now post original Image imgur link as comment`

#### `V1.0.2` Changes:
`-- Bot now has a config function to sleep for x seconds`
