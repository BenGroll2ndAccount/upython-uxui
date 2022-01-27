from string import whitespace
from uexceptions import uEXCEPTION_CUM, uEXCEPTION_TNMFT
from unodes import *
from tree import data
from graphics import *
import time
from helperclasses import *

def output(treedata):
    if "top" in treedata and treedata["top"] != None:
        print("################## Tree ##################")
        print(" ")
        root = uDISPLAY(treedata["top"]["properties"], treedata["top"]["child"], constrainX= int(treedata["top"]["properties"]["width"]), constrainY=int(treedata["top"]["properties"]["height"]), depth =  0)
        print(" ")
        dimensions = root.get_dimensions()
        return {
            "width" : dimensions["width"],
            "height" : dimensions["height"],
            "calls" : root.cue_draw_call([])
            }
    else:
        raise(uEXCEPTION_TNMFT)

    
def render_calls(zoom):
    render_data = output(data)
    display = GraphWin("PaperDisplay", render_data["width"]*zoom, render_data["height"]*zoom)

    ## DRAW CALL LOOP
    for call in render_data["calls"]:
        print(call.position)
        if call.__class__.__name__ == "udraw_Pixel":
            display.plotPixel(x = call.position.x, y = call.position.y, color = "black" if call.black else "white")
        elif call.__class__.__name__ == "udraw_Line":
            obj = Line(p1 = call.start.to_point() , p2 = call.start.to_point())
            obj.draw(display)
        elif call.__class__.__name__ == "udraw_Circle":
            obj = Circle(center = call.centerPoint.to_point(), radius=call.radius)
            obj.draw(display)
        elif call.__class__.__name__ == "udraw_Rect":
            print("here")
            if call.position != None:
                obj = Rectangle(p1 = call.position.to_point(), p2 = Point(call.position.x + call.width, call.position.y + call.height))
                obj.draw(display)
            else:
                obj = Rectangle(p1 = call.pointA.to_point(), p2 = call.pointB.to_point())
                obj.draw(display)

    input()

    
    #for x in range(render_data["width"]):
    #    for y in range(render_data["height"]):
    #        r = Rectangle(Point(x * zoom, y * zoom), Point(x * zoom + zoom, y * zoom + zoom))
    #        r.draw(display)    
render_calls(1)