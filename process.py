from PIL import Image

def processImageHSV(image):
    result = Image.new("HSV",image.size)
    print (image.format, image.size, "HSV")

    for x in range(image.size[0]):
        for y in range(image.size[1]):
            pixel = image.getpixel((x,y))
            # if it doesn't map to any known values
            result.putpixel( (x,y), pixel)

    return result

def getColors(image):
    print ("GetColorsMode")
    print(image.mode)

    myDict = {}
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            myDict[image.getpixel((x,y))] = True

    myList = []
    for key in myDict:
        myList.append(key)
    return myList 