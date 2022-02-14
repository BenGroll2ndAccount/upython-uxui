
from helperclasses import uConstrain
from low_level_nodes import *
import miscvalues as miscv
import systemvalues as sysv

class DISPLAY():
    def __init__(self, head):
        sysv.global_addL("darkmode_enabled", self)
        miscv.global_addL("debug_draw_constraints", self)
        self.head = head
        self.ready = head.assign_depth(0)
        self.output = head.output()
        self.last_draw_calls = head.draw()
        self.wallpaper = GraphWin("WallPaper", head.constraints.pointB.x, head.constraints.pointB.y)    
        self.redraw_all()
        input()

    def notify(self, name, value):
        if name == "darkmode_enabled":
            self.wallpaper.setBackground("black" if value else "white")
            self.last_draw_calls = self.head.draw()
        elif name == "debug_draw_constraints":
            self.last_draw_calls = self.head.draw()
        
    def redraw_all(self):
        calls = self.last_draw_calls
        for call in calls:
            
    
d = DISPLAY(
    uHEAD(
        constraints = uConstrain("constrain.rect", {"xA" : 0, "xB" : 880, "yA" : 0, "yB" : 528}),
        child = uPBOX(
            props={
            }
        )
    )
)