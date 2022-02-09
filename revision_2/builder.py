
from helperclasses import uConstrain
from low_level_nodes import *
import miscvalues as miscv
import systemvalues as sysv

'''
def build(top_node):
    ready = top_node.assign_depth(0)
    output = top_node.output()
    draw_calls = top_node.draw()
    wallpaper = GraphWin("WallPaper", top_node.constraints.pointB.x, top_node.constraints.pointB.y)
    
    for call in draw_calls:
'''     




class DISPLAY():
    def __init__(self, head):
        sysv.global_addL("darkmode_enabled", self)
        miscv.global_addL("debug_draw_constraints", self)
        self.head = head
        self.ready = head.assign_depth(0)
        self.output = head.output()
        self.last_draw_calls = head.draw()
        self.wallpaper = GraphWin("WallPaper", head.constraints.pointB.x, head.constraints.pointB.y)
        
            

        input()

    def notify(self, name, value):
        if name == "darkmode_enabled":
            self.wallpaper.setBackground("black" if value else "white")
            self.last_draw_calls = self.head.draw()
        elif name == "debug_draw_constraints":
            self.last_draw_calls = self.head.draw()
        
    def draw_calls(self, calls):
        for call in calls:
            if call.__class__.__name__ == "Point":




d = DISPLAY(
    uHEAD(
        constraints = uConstrain("constrain.rect", {"xA" : 0, "xB" : 880, "yA" : 0, "yB" : 528}),
        child = uPBOX(
            props={
            }
        )
    )
)