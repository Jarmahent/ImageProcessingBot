PImage img;
int mosaicSize = 12;
int pixelSkip = 0;
char moji = 'A';
String alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
String[] alphabetSplit = alphabet.split("");

void setup() {
  //size(640, 426);

  noStroke();
  img = loadImage("test3.jpg");
  surface.setSize(img.width, img.height);
}

void draw() {

  background(0);
  for(int y = 0; y < img.height; y+=mosaicSize, y = y + pixelSkip) {
    for(int x = 0; x < img.width; x+=mosaicSize, x = x + pixelSkip) {
      color c = img.get(x,y);
      fill(c);
      String random_letter = alphabetSplit[int(random(alphabetSplit.length))];
      textSize(20);

      text(random_letter ,x,y);
    }
  }
  noLoop();
}
