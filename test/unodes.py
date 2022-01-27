from uexceptions import *
from helperclasses import *
from drawcallclasses import *

class uNODE():
    def __init__(self, properties, child, constrainX, constrainY, depth):
        self.properties = properties
        self.child = child
        self.depth = depth
        self.hasChild = False
        if constrainX > 0 and constrainY > 0 and constrainX != None and constrainY != None:
            self.constrainX = constrainX
            self.constrainY = constrainY
        else:
            raise(uEXCEPTION_CUM(self.__class__.__name__))
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
        if child["type"] == "uDISPLAY":
            self.child = uDISPLAY(child["properties"], child["child"], depth= self.depth + 1, constrainY = self.constrain_modY(), constrainX = self.constrain_modX())
        elif child["type"] == "uRECT":
            self.child = uRECT(child["properties"], child["child"], depth=self.depth + 1, constrainY = self.constrain_modY(), constrainX = self.constrain_modX())
        else:
            raise uEXCEPTION_CBW(self.__class__.__name__, self.depth)
        
class uDISPLAY(uNODE):
    def getDrawCalls(self):
        return []

    def constrain_modX(self):
        return self.constrainX

    def constrain_modY(self):
        return self.constrainY

    def get_dimensions(self):
        return {
            "width" : self.properties["width"],
            "height" : self.properties["height"]
        }

class uRECT(uNODE):
    def getDrawCalls(self):
        try:
            width = self.properties["width"]
            height = self.properties["height"]
        except:
            raise uEXCEPTION_MRA
        position = self.properties["position"] if "position" in self.properties.keys() else uPoint(0, 0)
        thickness = self.properties["thickness"] if "thickness" in self.properties.keys() else 1
        round = self.properties["round"] if "round" in self.properties.keys() else False
        rounding = self.properties["rounding"] if "rounding" in self.properties.keys() else 0
        return [udraw_Rect(width=width, height=height, position=position, thickness=thickness, rounded=round, rounding=rounding)]

    def constrain_modX(self):
        return self.constrainX

    def constrain_modY(self):
        return self.constrainY

