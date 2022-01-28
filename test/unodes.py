from cgitb import small
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
                self.child = uDISPLAY(child["properties"], child["child"], depth= self.depth + 1, constrain = self.constrain_mod(), debug__draw_constraints = self.debug__draw_constraints)
            elif child["type"] == "uCARD":
                self.child = uCARD(child["properties"], child["child"], depth=self.depth + 1, constrain = self.constrain_mod(), debug__draw_constraints = self.debug__draw_constraints)
            else:
                raise uEXCEPTION_CBW(self.__class__.__name__, self.depth)

    def test_if_position_in_constraints(self, position, constrain):
        if constrain.shape == "constrain.rect":
            big_x = max(self.constrain.pointA.x, constrain.pointB.x)
            big_y = max(self.constrain.pointA.y, constrain.pointB.y)
            small_x = min(self.constrain.pointA.x, self.constrain.pointB.x)
            small_y = min(self.constrain.pointA.x, self.constrain.pointB.x)

            position = uPoint(x = position[0], y = position[1]) if "position" in self.properties.keys() else uPoint(0, 0)
            if position.x  > big_x or position.y > big_y or position.x < small_x or position.y < small_y:
                raise uEXCEPTION_WOB(self.__class__.__name__, self.depth)
            else:
                return True
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

class uCARD(uNODE):
    def getDrawCalls(self):
        try:
            width = self.properties["width"]
            height = self.properties["height"]
        except:
            raise uEXCEPTION_MRA
        self.test_if_position_in_constraints(position = self.properties["position"], constrain=self.constrain)
        self.test_if_position_in_constraints(position = (self.properties["position"][0] + self.properties["width"], self.properties["position"][1] + self.properties["height"]), constrain=self.constrain)
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

