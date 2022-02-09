class uEXCEPTION_TNMFT(Exception): # TOP NODE MISSING FROM TREE FILE
    def __init__(self):
        self.message = "Top Node is missing in tree file."
        super().__init__(self.message)

class uEXCEPTION_CUM(Exception): # CONSTRAINTS ON A WIDGET UNDER MINIMUM
    def __init__(self, causing_class, depth):
        self.message = "Constraints on a widget were under the minimum. Error Causing Widget: " + causing_class
        super().__init(self.message)

class uEXCEPTION_CBW(Exception): # COULDNT BUILD CHILD WIDGET
    def __init__(self, causing_class, depth):
        self.message = "Could not build child Widget. Error Causing Widget: " + causing_class + " @ " + str(depth)
        super().__init__(self.message)

class uEXCEPTION_MRA(Exception): # MISSING REQUIRED ATTRIBUTE
    def __init__(self, causing_class, depth):
        self.message = "Missing attribute with @required decorator. Error Causing Widget: " + causing_class + " @ " + str(depth)
        super().__init__(self.message)

class uEXCEPTION_RAE(Exception): # RECTANGLE ATTRIBUTE ERROR
    def __init__(self, causing_class, depth):
        self.message = "Either pointA and pointB OR position, width and height need to be specified. Error Causing Widget: " + causing_class + " @ " + str(depth)
        super().__init__(self.message)

class uEXCEPTION_WOB(Exception):
    def __init__(self, causing_class, depth):
        self.message = "Widget out of bounds of constraints given by parent widget. Error Causing Widget: " + causing_class + " @ " + str(depth)
        super().__init__(self.message)
