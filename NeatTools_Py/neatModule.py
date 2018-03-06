from graphics import *

class neatModule(Rectangle):

    def __init__(self, _x, _y, _color):
        modSize = 40
        Rectangle.__init__(self,Point(_x,_y),Point(_x + modSize, _y + modSize))
        self.color = _color