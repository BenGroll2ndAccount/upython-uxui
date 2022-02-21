from uexceptions import *
from graphics import *
class uPoint():
    def __init__(self, x : int, y : int):
        self.x = x
        self.y = y
        if x == None or y == None:
            raise uHELPEREXCEPTION("Node needs both, x and y, specified.", self.__class__.__name__)

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
                raise uHELPEREXCEPTION("Node needs all 4 values specified.", self.__class__.__name__)

    def out(self) -> str:
        return "(" + str(self.pointA.x) + "|" + str(self.pointA.y) + "),(" + str(self.pointB.x) + "|" + str(self.pointB.y) + ")"