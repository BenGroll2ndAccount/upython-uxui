from math import ldexp


global L_debug_draw_constraints
L_debug_draw_constraints = []

global debug_draw_constraints
debug_draw_constraints = False

class nMAP():
    def edit_debug_draw_constraints(value):
        global debug_draw_constraints
        global L_debug_draw_constraints
        debug_draw_constraints = value
        for listener in L_debug_draw_constraints:
            listener.notify("debug_draw_constraints", debug_draw_constraints)

    def add_debug_draw_constraints_listener(obj):
        global L_debug_draw_constraints
        L_debug_draw_constraints.append(obj)
    
    def remove_debug_draw_constraints_listener(obj):
        global L_debug_draw_constraints
        L_debug_draw_constraints.remove(obj)
        
    
def global_edit(name, value):
    func = getattr(nMAP, "edit_" + name)
    func(value)

def global_addL(name, obj):
    func = getattr(nMAP, "add_" + name + "_listener")
    func(obj)

def global_remL(name, obj):
    func = getattr(nMAP, "remove_" + name + "_listener")
    func(obj)

def global_remLALL(obj):
    pass