import getopt, glob, sys

import process

SUPPORTED_IMAGE_EXTENSIONS = ["png"]

def main(imageFolder, maskFile, colorMappingFile, outputFolder):
    print("ImageFolder: " + imageFolder)
    print("MaskFile: " + maskFile)
    print("Color Profile" + colorMappingFile)
    print("Output Folder: " + outputFolder)

    filesProcessed = 0

    # Pretty sure this doesn't search inside folders too
    for ext in SUPPORTED_IMAGE_EXTENSIONS:
        for fileName in glob.glob(imageFolder + "*." + ext):
            if process.processImage(fileName):
                filesProcessed += 1

    print ("Files Processed: " + str(filesProcessed))
    exit()

numArgs = len(sys.argv) - 1

# This parses arugments to make sure it's valid
if numArgs == 2:
    main(sys.argv[1], sys.argv[2], "./colorProfiles/edg32.colorProfile", "./output")
elif numArgs == 0:
    main("./images/", "mask.mask", "./colorProfiles/edg32.colorProfile", "./output")
else:
    print("Format <imageFolder> <maskFile> <colorProfile> <outputFolder>")
    exit()
    