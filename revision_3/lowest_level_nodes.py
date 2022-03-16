from udrawcalls import *
from uexceptions import *
from abc import abstractmethod
from typing import List
from unotifier import uNOTIFY
from helperclasses import *

class uNODE():
    def __node__init__(self, listening : List = None):
            for listen in listening:
                uNOTIFY.add_listener(listen, self)