

class uNOTIFIER:
    def __init__(self) -> None:
        self.darkmode_enabled = {"value" : False, "listening" : []}
        self.debug__draw_constraints = {"value" : False, "listening" : []}
        self.debug__draw_constraints_color = {"value" : "red", "listening" : []}
        self.debug__draw_rect_rounding_oct = {"value" : True, "listening" : []}
        
    def change(self, name, value):
        attr = getattr(self, name)
        attr["value"] = value
        for listener in attr["listening"]:
            listener.notify(name, value)

    def add_listener(self, name : str, obj):
        attr = getattr(self, name)
        attr["listening"].append(obj)

    def remove_listener(self, name : str, obj):
        attr = getattr(self, name)
        attr["listening"].remove(obj)

global uNOTIFY
uNOTIFY = uNOTIFIER()

