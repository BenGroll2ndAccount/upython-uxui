from uexceptions import uEXCEPTION_CUM, uEXCEPTION_TNMFT
from unodes import *
from tree import data
from graphics import *
from helperclasses import *
import debug as debug


global DARK_MODE_ENABLED
DARK_MODE_ENABLED = True 
'''
Defines Two-Color Colorspace, highlight and base
DARK_MODE_ENABLED => highlight = white
                     base = black

!DARK_MODE_ENABLED => highlight = black
                      base = white

'''

def output(treedata):
    if "top" in treedata and treedata["top"] != None:
        print("################## Tree ##################")
        print(" ")
        root = uDISPLAY(treedata["top"]["properties"], treedata["top"]["child"], depth =  0, constrain = uConstrain(shape = "constrain.rect", properties= {"xA" : 0, "yA" : 0, "xB" : 0, "yB" : 0}), debug__draw_constraints=debug.DEBUG_DRAW_CONSTRAINTS)
        print(" ")
        dimensions = root.get_dimensions()
        return {
            "width" : dimensions["width"],
            "height" : dimensions["height"],
            "calls" : root.cue_draw_call([])
            }
    else:
        raise(uEXCEPTION_TNMFT)

    
def render_calls():
    global DARK_MODE_ENABLED
    render_data = output(data)
    display = GraphWin("PaperDisplay", render_data["width"], render_data["height"])
    display.setBackground("black" if DARK_MODE_ENABLED else "white")
    display.setCoords(0, render_data["height"], render_data["width"], 0)
    print(render_data["calls"])
    ## DRAW CALL LOOP
    for call in render_data["calls"]:
        if call.__class__.__name__ == "udraw_Pixel":
            display.plotPixel(x = call.position.x, y = call.position.y, color = "black" if ((call.highlight and not DARK_MODE_ENABLED) or (not call.highlight and DARK_MODE_ENABLED)) else "white")
        elif call.__class__.__name__ == "udraw_Line":
            obj = Line(p1 = call.start.to_point() , p2 = call.start.to_point())
            obj.setOutline(color = "black" if ((call.highlight and not DARK_MODE_ENABLED) or (not call.highlight and DARK_MODE_ENABLED)) else "white")
            obj.draw(display)
        elif call.__class__.__name__ == "udraw_Circle":
            obj = Circle(center = call.centerPoint.to_point(), radius=call.radius)
            obj.setOutline(color = "black" if ((call.highlight and not DARK_MODE_ENABLED) or (not call.highlight and DARK_MODE_ENABLED)) else "white")
            obj.draw(display)
        elif call.__class__.__name__ == "udraw_Rect":
            if hasattr(call, "position"):
                obj = Rectangle(p1 = call.position.to_point(), p2 = Point(call.position.x + call.width, call.position.y + call.height))
                obj.setOutline("black" if ((call.highlight and not DARK_MODE_ENABLED) or (not call.highlight and DARK_MODE_ENABLED)) else "white") if not call.is_constraint else obj.setOutline(debug.DEBUG_DRAW_CONSTRAINTS_COLOR)
                obj.setFill("black" if ((call.highlight and not DARK_MODE_ENABLED) or (not call.highlight and DARK_MODE_ENABLED)) else "white") if call.filled and not call.is_constraint else None
                obj.draw(display)
            else:
                obj = Rectangle(p1 = call.pointA.to_point(), p2 = call.pointB.to_point())
                obj.setOutline("black" if ((call.highlight and not DARK_MODE_ENABLED) or (not call.highlight and DARK_MODE_ENABLED)) else "white") if not call.is_constraint else obj.setOutline(debug.DEBUG_DRAW_CONSTRAINTS_COLOR)
                obj.setFill("black" if ((call.highlight and not DARK_MODE_ENABLED) or (not call.highlight and DARK_MODE_ENABLED)) else "white") if call.filled and not call.is_constraint else None
                obj.draw(display)

    input()

    
    #for x in range(render_data["width"]):
    #    for y in range(render_data["height"]):
    #        r = Rectangle(Point(x * zoom, y * zoom), Point(x * zoom + zoom, y * zoom + zoom))
    #        r.draw(display)    
render_calls()