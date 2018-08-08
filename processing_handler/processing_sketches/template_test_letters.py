

def setup():
    global pixelSkip
    global alphabet
    global alphabetSplit
    global img

    pixelSkip = 10
    alphabetSplit = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

    img = loadImage("media/preprocessed/preprocessed.jpg")
    noStroke()
    noLoop()
    this.surface.setSize(img.width, img.height)


def draw():
    background(0)
    for y in range(0, img.height, pixelSkip):
        for x in range(0, img.width, pixelSkip):
            c = img.get(x, y)
            fill(c)
            random_letter = alphabetSplit[int(random(len(alphabetSplit)))]
            textSize(15)
            text(random_letter, x, y)

    save("../../media/processed/processed-test-letters.png")

    exit()
