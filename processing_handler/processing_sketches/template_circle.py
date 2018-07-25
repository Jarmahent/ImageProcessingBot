
def setup():
    global img
    img = loadImage("../media/preprocessed/preprocessed.jpg")
    this.surface.setSize(img.width, img.height)
    #global output
    #output = createWriter("positions.txt")


def draw():
    colorMode(HSB, 360, 100, 100)
    for y in range(0, img.height, 15):
        for x in range(0, img.width, 15):
            c = img.get(x, y)
            fill(c)
            noStroke()
            ellipse(x, y, 15, 15)


    #createGraphics(img.width, img.height)
    save("../../media/processed/processed.png")
    noLoop()
    exit()
