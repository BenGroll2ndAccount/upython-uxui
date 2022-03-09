from pickle import FALSE
from turtle import width
from udrawcalls import *
from uexceptions import *
from abc import abstractmethod
from typing import List
import miscvalues as miscv
import systemvalues as sysv
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
                    miscv.global_addL(splitentry[1], self)
                elif splitentry[0] == "sys":
                    sysv.global_addL(splitentry[1], self)

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
            for child in self.children:
                child.output()
        return

    def debugout(self):
        head = self.__class__.__name__ + "\n"
        message = head
        for prop in self.props.keys():
            message = message +  ">>>>" + prop + ": " + str(self.props[prop]) + "\n"
        return message

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
        self.constraints = value
        new_const = uConstrain(shape="constrain.rect", properties={"xA" : self.constraints.pointA.x, "xB" : self.constraints.pointB.x, "yA" : self.constraints.pointA.x, "yB" : self.constraints.pointB.y})
        if self.props["modXvalue"] != 100:
            modXfactor = self.props["modXvalue"] / 100
            whole_pixels_horizontal = self.constraints.width
            pixels_to_remove = whole_pixels_horizontal * (1 - modXfactor)    
            if self.props["alignX"] == "align.center":
                new_const.pointA.x += pixels_to_remove / 2
                new_const.pointB.x -= pixels_to_remove / 2
        if self.props["modYvalue"] != 100:
            modYfactor = self.props["modYvalue"] / 100
            whole_pixels_vertical = self.constraints.height
            pixels_to_remove = whole_pixels_vertical * (1 - modYfactor)
            if self.props["alignY"] == "align.center":
                new_const.pointA.y += pixels_to_remove / 2
                new_const.pointB.y -= pixels_to_remove / 2
        if self.child != None:
            self.child.constrainmod(new_const)

    def propmod(self):
        return self.props

    def draw(self):
        if self.child != None:
            childs_draws : List = self.child.draw()
            if miscv.debug_draw_constraints:
                childs_draws.append(udraw_Rectangle(pointA=self.constraints.pointA, pointB=self.constraints.pointB, is_debug=True))
            return childs_draws()
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
                filled = self.props["filled"],
                fill_match_border = self.props["fill_border"]
            )
        )
        if miscv.debug_draw_constraints:
            own_calls.append(
                udraw_Rectangle(pointA=self.constraints.pointA, pointB=self.constraints.pointB, is_debug=True)
            )
        if self.child != None:
            child_calls = self.child.draw()
            for call in child_calls:
                own_calls.append(call)
        return own_calls

class uROW(NODE):
    def check_for_buildtime_errors(self):
        pass
    def notify(name, value):
        raise NotImplementedError
    def constrainmod(self, value : uConstrain):
        self.constraints = value
        if self.children == None:
            return
        constwidth = value.width
        pixels_for_seperation = (self.props["seperator"] / 100) * constwidth
        pixels_for_constraints = constwidth - pixels_for_seperation
        pixels_for_each_seperator = pixels_for_seperation / (len(self.children) + 1) if self.props["include_edges"] == True else pixels_for_seperation / (len(self.children) - 1)
        pixels_for_each_widget = pixels_for_constraints / len(self.children)
        for index in range(len(self.children)):
            if self.props["include_edges"] and self.props["spacing"] == "spacing.equal":
                self.children[index].constrainmod(uConstrain(properties={
                    "xA" : self.constraints.pointA.x + pixels_for_each_widget * index + pixels_for_each_seperator * (index + 1),
                    "xB" : self.constraints.pointA.x + pixels_for_each_widget * (index + 1) + pixels_for_each_seperator * (index + 1),
                    "yA" : self.constraints.pointA.y,
                    "yB" : self.constraints.pointB.y,
                }))
            elif not self.props["include_edges"] and self.props["spacing"] == "spacing.equal":
                self.children[index].constrainmod(uConstrain(properties={
                    "xA" : self.constraints.pointA.x + pixels_for_each_widget * index + pixels_for_each_seperator * index,
                    "xB" : self.constraints.pointA.x + pixels_for_each_widget * (index + 1) + pixels_for_each_seperator * index,
                    "yA" : self.constraints.pointA.y,
                    "yB" : self.constraints.pointB.y
                }))

    def draw(self):
        children_calls = []
        for child in self.children:
            for draw_call in child.draw():
                children_calls.append(draw_call)
        if miscv.debug_draw_constraints:
            children_calls.append(udraw_Rectangle(pointA=self.constraints.pointA, pointB=self.constraints.pointB, is_debug=True))
        return children_calls

class uCOLUMN(NODE):
    def check_for_buildtime_errors(self):
        pass

    def notify(name, value):
        raise NotImplementedError

    def constrainmod(self, value : uConstrain):
        self.constraints = value
        if self.children == None:
            return
        constheight = value.height
        pixels_for_seperation = (self.props["seperator"] / 100) * constheight
        pixels_for_constraints = constheight - pixels_for_seperation
        pixels_for_each_seperator = pixels_for_seperation / (len(self.children) + 1) if self.props["include_edges"] == True else pixels_for_seperation / (len(self.children) - 1)
        pixels_for_each_widget = pixels_for_constraints / len(self.children)
        print(pixels_for_each_widget)
        print(pixels_for_seperation)
        for index in range(len(self.children)):
            if self.props["include_edges"] and self.props["spacing"] == "spacing.equal":
                self.children[index].constrainmod(uConstrain(properties={
                    "xA" : self.constraints.pointA.x,
                    "xB" : self.constraints.pointB.x,
                    "yA" : self.constraints.pointA.y + (pixels_for_each_widget + pixels_for_each_seperator) * (index + 1),
                    "yB" : self.constraints.pointB.y + pixels_for_each_widget * (index + 1) + pixels_for_each_seperator * (index + 1),
                }))
            elif not self.props["include_edges"] and self.props["spacing"] == "spacing.equal":
                self.children[index].constrainmod(uConstrain(properties={
                    "xA" : self.constraints.pointA.x,
                    "xB" : self.constraints.pointB.x,
                    "yA" : self.constraints.pointA.y + (pixels_for_each_widget + pixels_for_each_seperator) * index,
                    "yB" : self.constraints.pointB.y + (pixels_for_each_widget + pixels_for_each_seperator) * index + pixels_for_each_widget
                }))
    def draw(self):
        children_calls = []
        for child in self.children:
            for draw_call in child.draw():
                children_calls.append(draw_call)
        if miscv.debug_draw_constraints:
            children_calls.append(udraw_Rectangle(pointA=self.constraints.pointA, pointB=self.constraints.pointB, is_debug=True))
        return children_calls