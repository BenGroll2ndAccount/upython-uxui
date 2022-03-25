from udrawcalls import *
from uexceptions import *
from abc import abstractmethod
from typing import List
from unotifier import uNOTIFY
from helperclasses import *

class uNODE():
    def __node__init__(self, listening : List = None, level : int = 0):
        self.level = level
        if listening != None:
            for listen in listening:
                uNOTIFY.add_listener(listen, self)

    def assign_depth(self, value):
        self.depth = value
        if hasattr(self, "child") and self.child != None:
            self.child.assign_depth(self.depth + 1)
        elif hasattr(self, "children") and self.children != None:
            ready = [child.assign_depth(value + 1) for child in self.children]
            return
        return

    def printChild(self):
        print(self.child)
        if hasattr(self, "child") and self.child != None:
            self.child.printChild()
        if hasattr(self, "children") and self.children != None:
            for child in self.children:
                child.printChild()

    def output(self):
        constraintoutput = self.constraint.out()
        print((" " * 5 * self.depth) + self.__class__.__name__ + " " * (50 - len(self.__class__.__name__) - 5 * self.depth) + str(self.depth) + "-" + str(self.level) + "   " + constraintoutput )
        if not hasattr(self, "child") and not hasattr(self, "children"):
            return
        if hasattr(self, "child") and self.child != None:
            return self.child.output()
        if hasattr(self, "children") and self.children != None:
            return [child.output for child in self.children]

    
    @abstractmethod
    def notify(self, name, value):
        pass

    @abstractmethod
    def constrainmod(self, value):
        pass

    @abstractmethod
    def miscmod(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def __init__(self):
        pass

class uHEAD(uNODE):
    def __init__(self, width : int, height : int, child : uNODE, listening : List = None):
        self.width = width  
        self.height = height
        self.child = child
        self.__node__init__(listening=listening, level = 0)

    def notify(self, name, value):
        pass

    def constrainmod(self):
        self.constraint = uConstrain(pointA=uPoint(x=0, y=0), pointB=uPoint(x=self.width, y=self.height))
        return self.child.constrainmod(uConstrain(pointA=uPoint(x=0, y=0), pointB=uPoint(x=self.width, y=self.height)))

    def miscmod(self):
        return self.child.miscmod()

    def draw(self):
        return self.child.draw()

class uCARD(uNODE):
    def __init__(self, rounded : bool = False, rounding : int = False, filled : bool = True, fill_match_border : bool = False, highlight : bool = False, thickness : int = 1, child : uNODE = None, listening : List = None, level : int = 0):
        self.rounded = rounded
        self.rounding = rounding
        self.filled = filled
        self.fill_border = fill_match_border
        self.highlight = highlight
        self.child = child
        self.thickness = thickness
        self.__node__init__(listening=listening, level = level)

    def notify(self, name, value):
        pass

    def constrainmod(self, value : uConstrain):
        self.constraint = value
        if self.child != None:
            return self.child.constrainmod(uConstrain())
        else:
            return 0

    def miscmod(self):
        return self.child.miscmod()

    def draw(self):
        own_draw_calls = []
        if uNOTIFY.debug__draw_constraints:
            own_draw_calls.append(udraw_Rectangle(pointA = self.constraint.pointA, pointB = self.constraint.pointB, is_debug = True))
        own_draw_calls.append(udraw_Rectangle(pointA = self.constraint.pointA, pointB = self.constraint.pointB, border_is_highlight = self.highlight, thickness = self.thickness, rounding = self.rounding, round_oct = uNOTIFY.debug__draw_rect_rounding_oct, filled = self.filled, fill_match_border=self.fill_border, is_debug=False))
        if self.child != None:
            child_calls : List = self.child.draw()
        else:
            child_calls = []
        for call in own_draw_calls:
            child_calls.append(call)
        return child_calls
