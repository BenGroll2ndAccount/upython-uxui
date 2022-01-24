import builder
class NODE():
    def __init__(self, properties, child):
        self.properties = properties
        self.child = child
    
    def __cue_draw_call(self):
        self.cue_draw_call()

class DISPLAY(NODE):
    def cue_draw_call():
        pass

class PERCBOX(NODE):
    


def mapNode(type, data):
    if type == "DISPLAY":
        if "width" in data.keys and "height" in data.keys and data["width"] > 0 and data["height"] > 0:
            return DISPLAY(data["properties"], data["child"])
    else: