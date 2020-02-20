import pandas

from PIL import Image

import ColorScheme
import Mask
import Pixel

def parseMask(fileName):
    df = pandas.read_csv(fileName, usecols = ["label", "r", "g", "b"], dtype = {"label": "str", "r": "int", "g": "int", "b": "int"})
    numRows = len(df)
    
    mask = Mask.Mask()

    for index in range(numRows):
        pixel = Pixel.Pixel(df.iloc[index]['r'], df.iloc[index]['g'], df.iloc[index]['b'], "RGB")
        mask.addPixelLabel(df.iloc[index]['label'], pixel)

    return mask

def parseColorSchemes(fileName):
    df = pandas.read_csv(fileName, usecols = ["schemeLabel", "maskLabel", "r", "g", "b"], dtype = {"schemeLabel": "str", "maskLabel": "str", "r": "int", "g": "int", "b": "int"})
    numRows = len(df)

    myDict = dict()
    for index in range(numRows):
        schemeLabel = df.iloc[index]['schemeLabel']
        maskLabel = df.iloc[index]['maskLabel']
        pixel = Pixel.Pixel(df.iloc[index]['r'], df.iloc[index]['g'], df.iloc[index]['b'], "RGB")

        if schemeLabel not in myDict.keys():
            myDict[schemeLabel] = ColorScheme.ColorScheme(schemeLabel)            
        myDict[schemeLabel].addLabelPixel(maskLabel, pixel)

    colorSchemes = []
    for value in myDict.values():
        colorSchemes.append(value)    
    return colorSchemes 

#png format doesn't support HSV w/o conversion~
def processImageHSV(image: Image, mask: Mask, colorScheme: ColorScheme):
    pass

def processImageRGB(image: Image, mask: Mask, colorScheme: ColorScheme):
    pass

def processImageRGBA(image: Image, mask: Mask, colorScheme: ColorScheme):
    result = Image.new("RGBA",image.size)

    for x in range(image.size[0]):
        for y in range(image.size[1]):
            p = image.getpixel((x,y))
            p_r, p_g, p_b, p_a = p
            pixel = Pixel.Pixel(p_r, p_g, p_b, "RGB")
            
            pixelLabel = mask.getLabel(pixel)
            tPixel = colorScheme.getPixel(pixelLabel)
            if pixelLabel != "":
                result.putpixel( (x,y), (tPixel.r, tPixel.g, tPixel.b, p_a))
            else: # if it doesn't map to any known values
                result.putpixel( (x,y), p)

    return result

def getColors(image):
    myDict = {}
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            myDict[image.getpixel((x,y))] = True

    myList = []
    for key in myDict:
        myList.append(key)
    return myList 