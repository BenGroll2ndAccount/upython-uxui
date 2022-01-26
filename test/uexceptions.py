class uEXCEPTION_TNMFT(Exception):
    def __init__(self):
        self.message = "Top Node is missing in tree file."
        super().__init__(self.message)

class uEXCEPTION_CUM(Exception):
    def __init__(self, causing_class, depth):
        self.message = "Constraints on a widget were under the minimum. Error Causing Widget: " + causing_class
        super().__init(self.message)

class uEXCEPTION_CBW(Exception):
    def __init__(self, causing_class, depth):
        self.message = "Could not build child Widget. Error Causing Widget: " + causing_class + " @ " + str(depth)
        super().__init__(self.message)

class uEXCEPTION_MRA(Exception):
    def __init(self, causing_class, depth):
        self.message = "Missing attribute with @required decorator. Error Causing Widget: " + causing_class + " @ " + str(depth)
        super().__init__(self.message)