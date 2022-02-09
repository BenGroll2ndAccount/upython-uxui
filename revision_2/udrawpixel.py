from helperclasses import *
from uexceptions import *

class udraw_Pixel():
    def __init__(
                self, 
                position : uPoint,
                highlight : bool = True
                ):
        if position != None and highlight != None: # Requirance check
            self.position = position #Point Class
            self.highlight = highlight
        else:
            raise uDRAWEXCEPTION(widget = self.__class__.__name__, message = "")