class Pixel:
    mode: str = "RGB"
    #converted: bool = false

    r: int = 0
    g: int = 0
    b: int = 0

    h: int = 0
    s: int = 0
    v: int = 0

    def __init__(self, v1: int, v2: int, v3: int, mode: str):
        if mode == "RGB":
            self.mode = "RGB"
            self.r = v1
            self.g = v2
            self.b = v3
        else:
            self.mode = "HSV"
            self.h = v1
            self.s = v2
            self.v = v3

    def __hash__(self):
        return hash((self.r, self.g, self.b, self.h, self.s, self.v))

    def __eq__(self, other):
        if self.mode == other.mode:
            if (self.mode == "RGB"
                and self.r == other.r and self.g == other.g and self.b == other.b):
                return True
            elif (self.mode == "HSV"
                and self.h == other.h and self.s == other.s and self.v == other.v):
                return True
            return False
        else:
            return False

    def __ne__(self, other):
        if self == other:
            return False
        return True