class Pixel:
    def __init__(self, v1: int, v2: int, v3: int, mode: str):
        self.r = 0
        self.g = 0
        self.b = 0
        
        self.h = 0
        self.s = 0
        self.v = 0

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

    def __ne__(self, other):
        if self == other:
            return False
        return True