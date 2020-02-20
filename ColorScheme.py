import Mask
import Pixel

class ColorScheme:
    def __init__(self, name: str):
        self.name = name
        self.__labelPixelDict = dict()

    def canUseMask(self, mask: Mask):
        for label in mask.getLabels():
            if label not in self.__labelPixelDict:
                return False
        return True

    def addLabelPixel(self, label: str, pixel: Pixel):
        self.__labelPixelDict[label] = pixel

    # assume we validated mask already checked on this
    def getPixel(self, label: str):
        if label in self.__labelPixelDict:
            return self.__labelPixelDict[label]
        return Pixel.Pixel(255,0,255,"RGB")

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)