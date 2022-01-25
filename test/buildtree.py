from uexceptions import uEXCEPTION_CUM, uEXCEPTION_TNMFT
from unodes import *
from tree import data

def output(treedata):
    root = 0
    if "top" in treedata and treedata["top"] != None:
        root = uDISPLAY(treedata["top"]["properties"], treedata["top"]["child"], constrainX= int(treedata["top"]["properties"]["width"]), constrainY=int(treedata["top"]["properties"]["height"]), depth =  0)
    else:
        print("lmao")
        raise(uEXCEPTION_TNMFT)


output(data)
    
