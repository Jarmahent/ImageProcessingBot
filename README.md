![alt text](https://i.imgur.com/yztjtDY.png "Logo Title Text 1")

## Processing Images Bot for Reddit /r/processingimages

#### This bot uses the Processing language to take an a randomly selected image from any subreddit on Reddit.com and alters it.

#### Some premade sketches will be used from https://www.openprocessing.org/ please check it out.
Using the Processing.py Java compiler I am writing processing code in python.
Ex:

`mouse.py`

```python
def setup():
    size(400, 400)

def draw():
    background(255)
    fill(0)
    ellipse(mouseX, mouseY, 50, 50)
```
Using the commandline Processing Java compiler:

`java -jar processing-py.jar mouse.py`
