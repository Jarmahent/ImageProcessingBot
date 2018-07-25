
def setup():
    global img
    img = loadImage("../media/preprocessed/unprocessed.jpg")
    this.surface.setSize(img.width, img.height)
    global output
    output = createWriter("positions.txt")


def draw():
    colorMode(HSB, 360, 100, 100)
    for y in range(0, img.height, 10):
        for x in range(0, img.width, 10):
            output.println(x)
            x += 10
            c = img.get(x, y)
            fill(c)
            noStroke()
            ellipse(x, y, 1, 1)



    save("processed.png")
    noLoop()
