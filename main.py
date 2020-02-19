import getopt, glob, os, sys

from PIL import Image

import process

SUPPORTED_IMAGE_EXTENSIONS = ["png"]

def main(imageFolder, maskFile, colorMappingFile, outputFolder):
    print("ImageFolder: " + imageFolder)
    print("MaskFile: " + maskFile)
    print("Color Profile" + colorMappingFile)
    print("Output Folder: " + outputFolder)

    filesProcessed = 0

    try:
        os.makedirs(outputFolder)
    except OSError:
        print ("Folder already exists. Adding/overwriting data")
    else:
        print ("Created Output Folder")

    # Pretty sure this doesn't search inside folders too
    for ext in SUPPORTED_IMAGE_EXTENSIONS:
        for fileName in glob.glob(imageFolder + "*." + ext):
            filesProcessed += 1
            
            baseFileName = os.path.splitext(os.path.basename(fileName))[0]
            image = Image.open(fileName)
            hsvImage = image.convert("HSV")

            print ("Unique Colors (HSV):")
            print(process.getColors(hsvImage))
            process.processImageHSV(hsvImage)

            print ("Saving: "+ baseFileName + ".png")
            savePath = outputFolder + baseFileName + ".png"

            image.save(savePath)

    print ("Files Processed: " + str(filesProcessed))
    exit()

numArgs = len(sys.argv) - 1

# This parses arugments to make sure it's valid
if numArgs == 2:
    main(sys.argv[1], sys.argv[2], "./colorProfiles/edg32.colorProfile", "./output/")
elif numArgs == 0:
    main("./images/", "mask.mask", "./colorProfiles/edg32.colorProfile", "./output/")
else:
    print("Format <imageFolder> <maskFile> <colorProfile> <outputFolder>")
    exit()
    