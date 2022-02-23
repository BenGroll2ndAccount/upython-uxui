from cmath import rect
from turtle import shape
from udrawcalls import *
from uexceptions import *
from abc import abstractmethod
from typing import List
import miscvalues as misc
import systemvalues as sys
from helperclasses import *
from reqprops import propcheck

class NODE():
    def __init__(self, child = None, children : List = None, listening : List = None, props = None):
        self.props = propcheck(props, self.__class__.__name__)
        self.child = child
        self.children = children
        self.listening = listening
        if listening != None:
            for entry in listening:
                splitentry = entry.split(".")
                if splitentry[0] == "misc":
                    misc.global_addL(splitentry[1], self)
                elif splitentry[0] == "sys":
                    sys.global_addL(splitentry[1], self)

    def assign_depth(self, value):
        self.depth = value
        if self.child != None:
            return self.child.assign_depth(self.depth + 1)
        elif self.children != None:
            ready = [child.assign_depth(value + 1) for child in self.children]
            return 
        else:
            return 

    @abstractmethod
    def notify(self, name, value):
        pass
    @abstractmethod
    def check_for_buildtime_errors(self):
        pass
    @abstractmethod
    def constrainmod(self):
        pass
    @abstractmethod
    def propmod(self):
        pass
    @abstractmethod
    def draw(self):
        pass

    def printChild(self):
        print(self.child)
        if self.child != None:
            self.child.printChild()

    def output(self):
        constraintoutput = self.constraints.out()
        print((" " * 5 * self.depth) + self.__class__.__name__ + " " * (50 - len(self.__class__.__name__) - 5 * self.depth) + str(self.depth) + "   " + constraintoutput)
        if self.child == None and self.children == None:
            return
        if self.child != None:
            self.child.output()    
        elif self.children != None:
            for child in self.children():
                child.output()
        return

class uHEAD(NODE):
    def check_for_build_time_errors(self):
        if (self.child == None and self.children == None):
            raise uBUILDTIMEEXCEPTION("Node needs to have either child or children specified.", self.__class__.__name__)
        if (self.child != None and self.children != None):
            raise uBUILDTIMEEXCEPTION("Node cant have both child and children specified.", self.__class__.__name__)
        if self.children != None:
            raise uBUILDTIMEEXCEPTION("Node is not a multi-child node.", self.__class__.__name__)    
    def notify(name, value):
        raise NotImplementedError
    def constrainmod(self):
        self.constraints = uConstrain(shape="constrain.rect", properties={"xA" : 0, "yA" : 0, "xB" : self.props["width"], "yB" : self.props["height"]})
        print(self.constraints.out())
        self.child.constrainmod(self.constraints)
    def propmod(self):
        raise NotImplementedError
    def draw(self):
        return self.child.draw()

class uPBOX(NODE):
    def check_for_build_time_errors(self):
        if (self.child != None and self.children != None):
            raise uBUILDTIMEEXCEPTION("Node cant have both child and children specified." + self.__class__.__name__)
        if self.children != None:
            raise uBUILDTIMEEXCEPTION("Node is not a multi-child node.", self.__class__.__name__)   
        propcheck(self.__class__.__name__, self.props)

    def notify(name, value):
        raise NotImplementedError
    
    def constrainmod(self, value):
        const = value
        self.constraints = value
        new_const = self.constraints
        if "modX" in self.props.keys() and self.props["modX"]:
            width = max(const.pointA.x, const.pointB.x) - min(const.pointA.x, const.pointB.x)
            pixels_to_remove = width - width * self.props["modXvalue"] if "modXvalue" in self.props.keys() else 0
            if "alignX" in self.props.keys():
                if self.props["alignX"] == "align.center":
                    new_const.pointA.x += pixels_to_remove / 2
                    new_const.pointB.x -= pixels_to_remove / 2
                elif self.props["alignX"] == "align.start":
                    new_const.pointA.x += pixels_to_remove
                elif self.props["alignX"] == "align.end":
                    new_const.pointA.x -= pixels_to_remove
            else:
                new_const.pointA.x += pixels_to_remove / 2
                new_const.pointB.x -= pixels_to_remove / 2
        if "modY" in self.props.keys() and self.props["modY"]:
            height = max(const.pointA.x, const.pointB.x) - min(const.pointA.x, const.pointB.x)
            pixels_to_remove = height - height * self.props["modYvalue"] if "modYvalue" in self.props.keys() else 0
            if "alignY" in self.props.keys():
                if self.props["alignY"] == "align.center":
                    new_const.pointA.y += pixels_to_remove / 2
                    new_const.pointB.y -= pixels_to_remove / 2
                elif self.props["alignY"] == "align.start":
                    new_const.pointA.y += pixels_to_remove
                elif self.props["alignY"] == "align.end":
                    new_const.pointB.y -= pixels_to_remove
            else:
                new_const.pointA.y += pixels_to_remove / 2
                new_const.pointB.y -= pixels_to_remove / 2
        if self.child != None:
            self.child.constrainmod(new_const)

    def propmod(self):
        return self.props

    def draw(self):
        if self.child != None:
            return self.child.draw()
        else:
            return []
class uCARD(NODE):
    def check_for_build_time_errors(self):
        if (self.child != None and self.children != None):
            raise uBUILDTIMEEXCEPTION("Node cant have both child and children specified." + self.__class__.__name__)
        if self.children != None:
            raise uBUILDTIMEEXCEPTION("Node is not a multi-child node.", self.__class__.__name__)
    def notify(name, value):
        raise NotImplementedError
    
    def constrainmod(self, value : uConstrain):
        self.constraints = value        
        new_constraints = uConstrain(shape="constrain.rect", properties={"xA" : self.constraints.pointA.x, "xB" : self.constraints.pointB.x, "yA" : self.constraints.pointA.x, "yB" : self.constraints.pointB.y})
        new_constraints.pointA.x = new_constraints.pointA.x + self.props["thickness"]
        new_constraints.pointA.y = new_constraints.pointA.y + self.props["thickness"]
        new_constraints.pointB.x = new_constraints.pointB.x - self.props["thickness"]
        new_constraints.pointB.y = new_constraints.pointB.y - self.props["thickness"]
        if not self.child == None:
            self.child.constrainmod(new_constraints)
    def propmod(self):
        raise NotImplementedError

    def draw(self):
        own_calls = []
        own_calls.append(
            udraw_Rectangle(
                pointA = self.constraints.pointA,
                pointB = self.constraints.pointB,
                border_is_highlight = self.props["highlight"],
                thickness = self.props["thickness"],
                rounding = self.props["rounding"],
                round_oct = not self.props["rounded"],
            )
        )
        if self.child != None:
            child_calls = self.child.draw()
            for call in child_calls:
                own_calls.append(call)
        return own_calls
    