def setup():
    global img
    img = loadImage("media/preprocessed/preprocessed.jpg")
    this.surface.setSize(img.width, img.height)

    #global output
    #output = createWriter("positions.txt")


def draw():
    spacing = 20
    # this.surface.setVisible(False);
    colorMode(HSB, 360, 100, 100)
    for y in range(0, img.height, spacing):
        for x in range(0, img.width, spacing):
            c = img.get(x, y)
            fill(c)
            # noStroke()
            #randomSize = random(25)
            randomNoise = noise(10, 10)
            ellipseMode(CORNER)
            rectMode(CORNER)


            rect(x, y, 25, 25, 3)
            ellipse(x, y, 18, 18)




    save("../../media/processed/test-processed.png")
    noLoop()
    exit()
