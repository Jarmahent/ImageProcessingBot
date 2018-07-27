def setup():
    global img
    img = loadImage("media/preprocessed/preprocessed.jpg")
    this.surface.setSize(img.width, img.height)

    #global output
    #output = createWriter("positions.txt")


def draw():

    this.surface.setVisible(False);
    colorMode(HSB, 360, 100, 100)
    for y in range(0, img.height, 25):
        for x in range(0, img.width, 25):
            c = img.get(x, y)
            fill(c)
            noStroke()
            randomSize = random(25)
            ellipse(x, y, 25, 25)
            rect(x, y, 30, 30)

    save("../../media/processed/processed.png")
    noLoop()
    exit()
