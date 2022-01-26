from uexceptions import *

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
        print(self.child)
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
            raise uEXCEPTION_CBE(self.__class__.__name__, self.depth)
        
class uDISPLAY(uNODE):
    def getDrawCalls(self):
        return [self.__class__.__name__]

    def constrain_modX(self):
        return self.constrainX

    def constrain_modY(self):
        return self.constrainY

class uRECT(uNODE):
    def getDrawCalls(self):
        return [self.__class__.__name__]

    def constrain_modX(self):
        return self.constrainX

    def constrain_modY(self):
        return self.constrainY

