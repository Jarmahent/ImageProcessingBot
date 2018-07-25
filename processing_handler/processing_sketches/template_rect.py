
def setup():
    global img
    img = loadImage("../media/preprocessed/preprocessed.jpg")
    this.surface.setSize(img.width, img.height)
    #global output
    #output = createWriter("positions.txt")


def draw():


    colorMode(HSB, 360, 100, 100)
    for y in range(0, img.height, 10):
        for x in range(0, img.width, 10):
            c = img.get(x, y)
            fill(c)
            noStroke()
            randomSize = random(25)
            #ellipse(x, y, 10, 10)
            rect(x, y, 10, 10)

    #createGraphics(img.width, img.height)

    save("../../media/processed/processed.png")
    noLoop()
    exit()
