from low_level_nodes import *
import miscvalues as miscv
import systemvalues as sysv

class DISPLAY():
    def __init__(self, head):
        sysv.global_addL("darkmode_enabled", self)
        miscv.global_addL("debug_draw_constraints", self)
        self.head = head
        self.ready = self.head.assign_depth(0)
        self.ready = self.head.constrainmod()
        self.ready = self.head.output()
        self.last_draw_calls = head.draw()
        #self.head.printChild()
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
        print(calls)
        highlight_color = "white" if sysv.darkmode_enabled else "black"
        background_color = "black" if sysv.darkmode_enabled else "white"
        for call in calls:
            if call.__class__.__name__ == "udraw_Rectangle":
                obj = Rectangle(call.pointA.to_point(), call.pointB.to_point())
                obj.setOutline(highlight_color if call.border_is_highlight else background_color)
                obj.setFill(highlight_color if call.border_is_highlight else background_color)
                obj.setWidth(call.thickness)
                obj.draw(self.wallpaper)

tree = uHEAD(
    props = {
    "width":880,
    "height":528,
    },
    child=uCARD(
        props={
            "thickness" : 10
        },
        child=uCARD(
            props={
                "thickness" : 5,
                "border_is_highlight" : False
            },
            child=uCARD(
                props={
                    "thickness" : 5,
                    "border_is_highlight" : True
                }
            )
        )
    )
    )
 

wallpaper = DISPLAY(
    head = tree
)

    
