import graphics
from unotifier import uNOTIFY
from lowest_level_nodes import *


rootnode = uHEAD(
    width=880,
    height=528,
    child=uCARD(
        listening=["darkmode_enabled"]
    ))

class ROOT:
    def build(self, rootnode = rootnode):
        self.wallpaper = graphics.GraphWin("Wallpaper", width=rootnode.width, height = rootnode.height)
        uNOTIFY.add_listener("darkmode_enabled", self)
        ##Startup Cycles
        print("Started Depth Cycle")
        wait = rootnode.assign_depth(0)
        print("Finished Depth Cycle")
        print("Started Constrainmod Cycle")
        wait = rootnode.constrainmod()
        print("Finished Constrainmod Cycle")
        print("Started Draw Cycle")
        draw_calls = rootnode.draw()
        print("Finished Draw Cycle")
        print("Started Output Cycle")
        print("-------------------")
        print("Type" + " " * (50 - len("Type")) + "Depth" + " " + "Constraints")
        print(" ")
        wait = rootnode.output()
        print("-------------------")
        input()

_WALLPAPER_ = ROOT()
_WALLPAPER_.build()
