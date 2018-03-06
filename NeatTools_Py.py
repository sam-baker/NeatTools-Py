from graphics import *
from NeatTools_Py.neatPoint import *
from NeatTools_Py.neatModule import *


def main():
    win = GraphWin("My Window", 500, 500)
    win.setBackground(color_rgb(255,200,23))
    
    pt = neatPoint(25,25, color_rgb(0,0,0))
    myModule = neatModule(20,20,color_rgb(44,222,33))

    myModule.draw(win)

    pt1 = Point(pt.x, pt.y)
    pt2 = Point(250, 350)
    pt1.draw(win)

    win.getMouse()
    win.close()

main()