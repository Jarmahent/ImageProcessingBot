def setup(): #Loads an image onto the canvas.
    img = PImage()

    size(400, 400)

def draw():
    img = loadImage("carbon.jpg");
    image(img, 0, 0);
    fill(0)
    ellipse(mouseX, mouseY, 50, 50)
