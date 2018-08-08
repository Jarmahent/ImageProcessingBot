def setup():
    global img, x, y, totalImg

    img = loadImage("media/preprocessed/preprocessed.jpg")
    x, y = 0, 0
    totalImg = img.width*img.height

    this.surface.setSize(img.width, img.height)
    strokeWeight(3)
    background(0)
    noLoop()

def draw():
    global x, y, img, totalImg

    for i in range(0, totalImg):
        c = img.get(x, y)
        stroke(c)
        if random(1) < .5:
            line(x, y, x+10, y+10)
        else:
            line(x ,y+10, x+10, y);
        x+=10
        if(x>width):
            x = 0
            y+=10

    save("../../media/processed/processed.png")
    exit()
