from PIL import Image

def processImage(imageFileName):
    print ("processing file: " + imageFileName)

    image = Image.open(imageFileName)
    print (image.format, image.size, image.mode)

    return True