class EXCEPTION_TNMFT(Exception):
    def __init__(self):
        self.message = "Top Node is missing in tree file."
        super().__init__(self.message)