import Pixel

class Mask:
    __pixelLabelDict = dict()

    def addPixelLabel(self, pixel: Pixel, label: str):
        self.__pixelLabelDict[pixel] == label

    def getLabel(self, pixel: Pixel):
        if pixel in self.__pixelLabelDict.keys():
            return self.__pixelLabelDict[pixel]
        return ""
    
    def getLabels(self):
        result = []
        for value in self.__pixelLabelDict.values():
            result.append(value)
        return result