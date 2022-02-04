from uexceptions import *
from abc import abstractmethod
from typing import List
import miscvalues as misc
import systemvalues as sys
from helperclasses import *

def NODE():
    def __init__(self, constraints : uConstrain, child : NODE = None, children : List = None, listening : List = None, props = None):
        self.constraints = constraints
        self.child = child
        self.children = children
        self.listening = listening
        self.props = props
        for entry in listening:
            splitentry = entry.split(".")
            if splitentry[0] == "misc":
                misc.global_addL(splitentry[1], self)
            elif splitentry[0] == "sys":
                sys.global_addL(splitentry[1], self)

    def assign_depth(self, value):
        self.depth = value
        if self.child != None:
            return self.child.assign_depth(self.depth + 1)
        elif self.children != None:
            ready = [child.assign_depth(value + 1) for child in self.children]
            return True
        else:
            return True

    @abstractmethod
    def notify(self, name, value):
        pass
    @abstractmethod
    def check_for_buildtime_errors(self):
        pass
    @abstractmethod
    def constrainmod(self):
        pass
    @abstractmethod
    def propmod(self):
        pass
    @abstractmethod
    def draw(self):
        pass
    @abstractmethod
    def output(self):
        print((" " * 5 * self.depth) + self.__class__.__name__ + " " * (50 - len(self.__class__.__name__) - 5 * self.depth) + str(self.depth))
        if self.child != None:
            self.child.output()    
        elif self.children != None:
            for child in self.children():
                child.output()


def uPBOX(NODE):
    def check_for_build_time_errors(self):
        if (self.child != None and self.children != None):
            raise uBUILDTIMEEXCEPTION("Node cant have both child and children specified." + self.__class__.__name__)
        if self.children != None:
            raise uBUILDTIMEEXCEPTION("Node is not a multi-child node.", self.__class__.__name__)    
    def notify(name, value):
        raise NotImplementedError
    def constrainmod():
        raise NotImplementedError
    def propmod():
        raise NotImplementedError
    def draw():
        raise NotImplementedError

def uHEAD(NODE):
    def check_for_build_time_errors(self):
        if (self.child == None and self.children == None):
            raise uBUILDTIMEEXCEPTION("Node needs to have either child or children specified.", self.__class__.__name__)
        if (self.child != None and self.children != None):
            raise uBUILDTIMEEXCEPTION("Node cant have both child and children specified.", self.__class__.__name__)
        if self.children != None:
            raise uBUILDTIMEEXCEPTION("Node is not a multi-child node.", self.__class__.__name__)    
    def notify(name, value):
        raise NotImplementedError
    def constrainmod():
        raise NotImplementedError
    def propmod():
        raise NotImplementedError
    def draw():
        raise NotImplementedError


    