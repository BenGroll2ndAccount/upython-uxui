from distutils.command.build import build
from graphics import *
from testtree import treedata
from test.uexceptions import *
from nodes import *


def buildChild(data):
    if data == None:
        return None
    return mapNode(type = data["type"], properties=data["properties"], child=buildChild(data["child"]))


def _build_object_tree(data):
    try:
        t = data["top"]
    except:
        raise uEXCEPTION_CUM
    data = data["top"]
    topnode = DISPLAY(data["properties"], buildChild(data["child"]))
    _tree_out(topnode)
    


def print_node(data, offset):
    if data == None:
        return
    print((" " * (offset) + "ட " + str(data.type)).format(""))
    print_node(data.child, offset + 5)

def _tree_out(node):
    print_node(node, 0)


def _render(data, zoom):
    display = GraphWin("PaperDisplay", len(data[0])*zoom, len(data)*zoom)
    print(str(len(data[0])*zoom) + " x " + str(len(data)*zoom))
    for x in range(len(data[0])):
        for y in range(len(data)):
            r = Rectangle(Point(x * zoom, y * zoom), Point(x * zoom + zoom, y * zoom + zoom))
            r.setFill("black") if data[y][x] else r.setFill("white")
            r.draw(display)
    input()


_build_object_tree(treedata)