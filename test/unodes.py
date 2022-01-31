from cgitb import small
from lib2to3.pytree import Node
from turtle import position
from uexceptions import *
from helperclasses import *
from drawcallclasses import *

class uNODE():
    def __init__(self, properties, child, constrain : uConstrain, depth, debug__draw_constraints = False):
        self.properties = properties
        self.child = child
        self.depth = depth
        self.hasChild = False
        self.constrain = constrain
        self.debug__draw_constraints = debug__draw_constraints
        self.output()
        
        
    def output(self):
        print((" " * 5 * self.depth) + self.__class__.__name__ + " " * (50 - len(self.__class__.__name__) - 5 * self.depth) + str(self.depth))

    def cue_draw_call(self, data):
        self.attachChild(self.child)
        own_calls = self.getDrawCalls()
        for call in own_calls:
            data.append(call)
        if self.child != None:
            return self.child.cue_draw_call(data)
        else:
            return data
        
    def attachChild(self, child):
        if child == None:
            return
        if "child" in child.keys():
            if child["type"] == "uDISPLAY":
                self.child = uDISPLAY(properties = self.propmod(child["properties"]), child = child["child"], depth= self.depth + 1, constrain = self.constrain_mod(), debug__draw_constraints = self.debug__draw_constraints)
            elif child["type"] == "uCARD":
                self.child = uCARD(properties = self.propmod(child["properties"]), child = child["child"], depth=self.depth + 1, constrain = self.constrain_mod(), debug__draw_constraints = self.debug__draw_constraints)
            else:
                raise uEXCEPTION_CBW(self.__class__.__name__, self.depth)

    def test_if_position_in_constraints(self, position):
        if self.constrain.shape == "constrain.rect":
            big_x = max(self.constrain.pointA.x, self.constrain.pointB.x)
            big_y = max(self.constrain.pointA.y, self.constrain.pointB.y)
            small_x = min(self.constrain.pointA.x, self.constrain.pointB.x)
            small_y = min(self.constrain.pointA.x, self.constrain.pointB.x)
            position = uPoint(x = position[0], y = position[1]) if "position" in self.properties.keys() else uPoint(0, 0)
            if position.x > small_x and position.x < big_x and position.y > small_y and position.y < big_y:
                return True
            else:
                raise uEXCEPTION_WOB(self.__class__.__name__, self.depth)
        return True
        
        
class uDISPLAY(uNODE):
    def getDrawCalls(self):
        return []

    def constrain_mod(self) -> uConstrain:
        return uConstrain("constrain.rect", {"xA" : 0, "yA" : 0, "xB" : self.properties["width"], "yB" : self.properties["height"]})


    def get_dimensions(self):
        return {
            "width" : self.properties["width"],
            "height" : self.properties["height"]
        }

    def propmod(self, data):
        return data

class uCARD(uNODE):
    def getDrawCalls(self):
        try:
            width = self.properties["width"]
            height = self.properties["height"]
        except:
            raise uEXCEPTION_MRA
        self.test_if_position_in_constraints(position = self.properties["position"])
        print((self.properties["position"][0] + self.properties["width"], self.properties["position"][1] + self.properties["height"]))
        self.test_if_position_in_constraints(position = (self.properties["position"][0] + self.properties["width"], self.properties["position"][1] + self.properties["height"]))
        thickness = self.properties["thickness"] if "thickness" in self.properties.keys() else 1
        round = self.properties["round"] if "round" in self.properties.keys() else False
        rounding = self.properties["rounding"] if "rounding" in self.properties.keys() else 0
        filled = self.properties["filled"] if "filled" in self.properties.keys() else False
        fill_highlight = self.properties["fill-highlight"] if "fill-highlight" in self.properties.keys() else False
        data = []
        position = uPoint(self.properties["position"][0], self.properties["position"][1])
        data.append(udraw_Rect(width=width, height=height, position=position, thickness=thickness, rounded=round, rounding=rounding, filled = filled, fill_highlight = fill_highlight))
        if self.debug__draw_constraints:
            data.append(udraw_Rect(pointA = self.constrain.pointA, pointB=self.constrain.pointB, is_constraint=True))
        return data

    def constrain_mod(self) -> uConstrain:
        return uConstrain(
            shape="constrain.rect",
            properties = {
                "xA" : self.properties["position"][0] if "position" in self.properties.keys() else self.pointA.x,
                "yA" : self.properties["position"][1] if "position" in self.properties.keys() else self.pointA.y,
                "xB" : self.properties["position"][0] + self.properties["width"] if "width" in self.properties.keys() else self.pointB.x,
                "yB" : self.properties["position"][1] + self.properties["height"] if "height" in self.properties.keys() else self.pointB.y
            }
        )

    def propmod(self, data):
        return data

class uPBOX(uNODE):
    def getDrawCalls(self):
        return []

    def constrain_mod(self) -> uConstrain:
        child_constrain = uConstrain(shape = "constrain.rect", properties={})
        if self.properties["modX"]:
            width = self.constrain.pointB.x - self.constrain.pointA.x
            pixels_total = width - width * self.properties["modXvalue"]
            if self.properties["alignX"] == "align.center":
                newSmallX = self.constrain.pointA.x + (0.5 * pixels_total)
                newBigX = self.constrain.pointB.x - (0.5 * pixels_total)
            elif self.properties["alignX"] == "align.start":
                newSmallX = self.constrain.pointA.x + pixels_total
                newBigX = self.constrain.pointB.x
            elif self.properties["alignX"] == "align.end":
                newSmallX = self.constrain.pointA.x
                newBigX = self.constrain.pointB.x - pixels_total
        if self.properties["modY"]:
            pass 

        
        height = self.constrain.pointB.y - self.constrain.pointA.y

        
        
    def propmod(self, data):
        return data

