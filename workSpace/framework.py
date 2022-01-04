import json

class DISPLAY:
    def __init__(self, width, height, child):
        self.width = width
        self.height = height
        self.child = child

class COMPONENT:
    def __init__(self, uind):
        self.uind = uind
