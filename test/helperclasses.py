from uexceptions import *
from graphics import *
class uPoint():
    def __init__(self, x : int, y : int):
        self.x = x
        self.y = y
        if x == None or y == None:
            raise uEXCEPTION_MRA(self.__class__.__name__, depth = "<helper>")

    def to_point(self) -> Point:
        return Point(x = self.x, y = self.y)


class uConstrain():
    def __init__(self, shape : str, properties):
        self.shape = shape
        self.properties = properties
        if shape == "constrain.rect":
            if "xA" in properties.keys() and "yA" in properties.keys() and "xB" in properties.keys() and "yB" in properties.keys():
                self.pointA = uPoint(x = properties["xA"], y = properties["yA"])
                self.pointB = uPoint(x = properties["xB"], y = properties["yB"])
            else:
                raise uEXCEPTION_MRA(self.__class__.__name__, depth = "<helper>")