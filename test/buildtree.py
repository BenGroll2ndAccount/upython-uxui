from uexceptions import uEXCEPTION_CUM, uEXCEPTION_TNMFT
from unodes import *
from tree import data

def output(treedata):
    if "top" in treedata and treedata["top"] != None:
        root = uDISPLAY(treedata["top"]["properties"], treedata["top"]["child"], constrainX= int(treedata["top"]["properties"]["width"]), constrainY=int(treedata["top"]["properties"]["height"]), depth =  0)
        print(root.cue_draw_call([]))
    else:
        raise(uEXCEPTION_TNMFT)


output(data)
    
