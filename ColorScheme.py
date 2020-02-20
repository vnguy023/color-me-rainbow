import Mask
import Pixel

class ColorScheme:
    __labelPixelDict = dict()

    def __init__(self, name: str):
        self.name = name

    def canUseMask(self, mask: Mask):
        for label in mask.getLabels():
            if self.__labelPixelDict.get(label) != 1:
                return False
        return True

    def addLabelPixel(self, label: str, pixel: Pixel):
        self.__labelPixelDict[label] = pixel

    def getPixel(self, label: str):
        if label in self.__labelPixelDict.keys():
            return self.__labelPixelDict[label]
        else:
            if label != "":
                print ("[ColorScheme::getPixel()] [Error=label does not exist] [label=" + label + "]")
            return False

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)