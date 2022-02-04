
from helperclasses import uConstrain
from low_level_nodes import *


def build(top_node):
    ready = top_node.assign_depths()
    output = top_node.output()
    draw_calls = top_node.cue_draw_calls()

build(uHEAD(
    constraints = uConstrain("constrain.rect", {"xA" : 0, "xB" : 880, "yA" : 0, "yB" : 528}),
    child = uPBOX(
        constraints = uConstrain("constrain.rect", {"xA" : 0, "xB" : 880, "yA" : 0, "yB" : 528})
    )
))