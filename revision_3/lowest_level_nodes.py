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

    def assign_depth(self, value):
        self.depth = value
        if self.child != None:
            self.child.assign_depth(self.depth + 1)
        elif self.children != None:
            ready = [child.assign_depth(value + 1) for child in self.children]
            return
        return

    def printChild(self):
        print(self.child)
        if self.child != None:
            self.child.printChild()
        if self.children != None:
            for child in self.children:
                child.printChild()

    def output(self):
        constraintoutput = self.constraints.out()
        print((" " * 5 * self.depth) + self.__class__.__name__ + " " * (50 - len(self.__class__.__name__) - 5 * self.depth) + str(self.depth) + "   " + constraintoutput)
        if self.child == None and self.children == None:
            return
        if self.child != None:
            self.child.output()    
        elif self.children != None:
            for child in self.children:
                child.output()
        return

    def debugout(self):
        head = self.__class__.__name__ + "\n"
        message = head
        for prop in self.props.keys():
            message = message +  ">>>>" + prop + ": " + str(self.props[prop]) + "\n"
        return message
    
    @abstractmethod
    def notify(self, name, value):
        pass

    @abstractmethod
    def constrainmod(self, value):
        pass

    @abstractmethod
    def miscmod(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    