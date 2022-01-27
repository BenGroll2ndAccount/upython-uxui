from uexceptions import *
from graphics import *
class uPoint():
    def __init__(self, x : int, y : int):
        self.x = x
        self.y = y
        if x == None or y == None:
            raise uEXCEPTION_MRA(self.__class__.__name__, depth = "")

    def to_point(self) -> Point:
        return Point(x = self.x, y = self.y)