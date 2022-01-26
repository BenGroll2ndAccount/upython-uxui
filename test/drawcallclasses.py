
class udraw_Pixel():
    def __init__(self, position, black):
        self.position = position #Point Class
        self.black = black

class udraw_Line():
    def __init__(self, start, end, black):
        self.start = start
        self.end = end
        self.black = black

class udraw_Rect():
    def __init__(self, position, width, height, thickness, rounded, rounding):
        self.position = position
        self.width = width
        self.height = height
        self.thickness = thickness
        self.rounded = rounded
        self.rounding = rounding

