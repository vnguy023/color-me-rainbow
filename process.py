import json

from PIL import Image

import ColorScheme
import Mask
import Pixel

def parseMask(fileName):
    mask = Mask.Mask()
    return mask

def parseColorSchemes(fileName):
    colorSchemes = []
    colorSchemes.append(__parseColorScheme())
    return colorSchemes

def __parseColorScheme():
    return ColorScheme.ColorScheme("default")

#png format doesn't support HSV w/o conversion~
def processImageHSV(image: Image, mask: Mask, colorScheme: ColorScheme):
    result = Image.new("HSV",image.size)
    print (image.format, image.size, "HSV")

    for x in range(image.size[0]):
        for y in range(image.size[1]):
            p = image.getpixel((x,y))
            p_h, p_s, p_v = p
            pixel = Pixel.Pixel(p_h, p_s, p_v, "HSV")
            
            pixelLabel = mask.getLabel(pixel)
            tPixel = colorScheme.getPixel(pixelLabel)
            if pixelLabel != "" and tPixel != False:
                result.putpixel( (x,y), (tPixel.h, tPixel.s, tPixel.v))
            else: # if it doesn't map to any known values
                result.putpixel( (x,y), p)

    return result

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
            if pixelLabel != "" and tPixel != False:
                result.putpixel( (x,y), (tPixel.r, tPixel.g, tPixel.b), p_a)
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