import getopt, glob, os, sys

from PIL import Image

import process
import ColorScheme
import Mask

SUPPORTED_IMAGE_EXTENSIONS = ["png"]

def main(imageFolder, maskFileName, colorSchemeFileName, outputFolder):
    print("ImageFolder: " + imageFolder)
    print("MaskFileName: " + maskFileName)
    print("ColorSchemeFileName" + colorSchemeFileName)
    print("Output Folder: " + outputFolder)

    filesProcessed = 0

    try:
        os.makedirs(outputFolder)
    except OSError:
        print ("Folder already exists. Adding/overwriting data")
    else:
        print ("Created Output Folder")

    mask = process.parseMask(maskFileName)
    colorSchemes = process.parseColorSchemes(colorSchemeFileName)

    for colorScheme in colorSchemes:
        if colorScheme.canUseMask(mask) == False:
            print("[Error=ColorScheme can't use mask] [colorScheme=" + colorScheme.name + "]")
            exit()

    # Pretty sure this doesn't search inside folders too
    for ext in SUPPORTED_IMAGE_EXTENSIONS:
        for fileName in glob.glob(imageFolder + "*." + ext):
            filesProcessed += 1
            
            baseFileName = os.path.splitext(os.path.basename(fileName))[0]
            image = Image.open(fileName)
            #hsvImage = image.convert("HSV")
            rgbaImage = image.convert("RGBA")

            print ("GetColors: mode=" + rgbaImage.mode)
            print (process.getColors(rgbaImage))
            
            for colorScheme in colorSchemes:
                result = process.processImageRGBA(rgbaImage, mask, colorScheme)

                saveFileName = baseFileName + "_" + colorScheme.name
                savePath = outputFolder + saveFileName + ".png"

                print ("Saving: " + saveFileName + ".png")
                result.save(savePath)

    print ("Files Processed: " + str(filesProcessed))
    exit()

numArgs = len(sys.argv) - 1

# This parses arugments to make sure it's valid
if numArgs == 2:
    main(sys.argv[1], sys.argv[2], "./colorSchemes/edg32.csv", "./output/")
elif numArgs == 0:
    main("./images/", "./masks/sampleMaskRGB.csv", "./colorSchemes/edg32.csv", "./output/")
else:
    print("Format <imageFolder> <maskFileName> <colorSchemeFileName> <outputFolder>")
    exit()
    