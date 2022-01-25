from uexceptions import uEXCEPTION_CUM


class uNODE():
    def __init__(self, properties, child, constrainX, constrainY, depth):
        self.properties = properties
        self.child = child
        self.depth = depth
        if constrainX > 0 and constrainY > 0 and constrainX != None and constrainY != None:
            self.constrainX = constrainX
            self.constrainY = constrainY
        else:
            raise(uEXCEPTION_CUM(self.__class__.__name__))
        self.output()
        self.attachChild(self.child)
        
    def output(self):
        print((" " * 5 *self.depth) + self.__class__.__name__ + "    -    " + str(self.depth))

    def __cue_draw_call(self):
        self.getDrawCalls()
        if self.child != None:
            self.child.__cue_draw_call()

    def attachChild(self, child):
        if child == None:
            return
        if child["type"] == "uDISPLAY":
            child = uDISPLAY(child["properties"], child["child"], depth= self.depth + 1, constrainY = self.constrain_modY(), constrainX = self.constrain_modX())
        elif child["type"] == "uRECT":
            child = uRECT(child["properties"], child["child"], depth=self.depth + 1, constrainY = self.constrain_modY(), constrainX = self.constrain_modX())
        
class uDISPLAY(uNODE):
    def getDrawCalls(self):
        pass

    def constrain_modX(self):
        return self.constrainX

    def constrain_modY(self):
        return self.constrainY

class uRECT(uNODE):
    def getDrawCalls(self):
        pass

    def constrain_modX(self):
        return self.constrainX

    def constrain_modY(self):
        return self.constrainY

