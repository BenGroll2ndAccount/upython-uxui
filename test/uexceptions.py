class uEXCEPTION_TNMFT(Exception):
    def __init__(self):
        self.message = "Top Node is missing in tree file."
        super().__init__(self.message)

class uEXCEPTION_CUM(Exception):
    def __init__(self, causing_class):
        self.message = "Constraints on a widget were under the minimum. Error Causing Widget: " + causing_class
        super().__init(self.message)