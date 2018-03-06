from graphics import *

class neatPoint:
    pt = Point(245,25)
    pt.setOutline(color_rgb(0,0,0))

    def __init__(self, x, y,color):
        self.x = x
        self.y = y
        self.color = color
