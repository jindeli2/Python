import graphics as g
win = g.GraphWin( " Graphics Window ", 710, 650 )

def drawOutline():
    House = g.Rectangle( g.Point(40, 110), g.Point(440, 500))
    House.draw( win )
    House.setOutline("Brown")

def drawWindows():
    rightW = g.Rectangle(g.Point(80, 150), g.Point(200, 250))
    rightW.draw(win)
    rightW.setOutline("Light Green")
    leftW = rightW.clone()
    leftW.move(200, 0)
    leftW.draw(win)
 
def drawRoof():
    door = g.Rectangle(g.Point(200, 350), g.Point(300, 500))
    door.draw(win)
    rightL = g.Line(g.Point(40, 110), g.Point(240, 10))
    rightL.draw(win)
    leftL = g.Line(g.Point(440, 110), g.Point(240, 10))
    leftL.draw(win)

def drawHouseBoard():
    Lable = g.Text( g.Point(390,430), "My House!")
    Lable.setOutline("Blue")
    Lable.draw(win)


def drawHouse():
    drawOutline()
    drawWindows()
    drawRoof()
    drawHouseBoard()

def drawSun():
    sunDot = g.Point(530,50)
    sun = g.Circle(sunDot, 40)
    sun.setFill("Orange")
    sun.setOutline("Red")
    sun.draw(win)
    win.getMouse()
    sun.move(33, 113)
    win.setBackground("grey")
    sun.setFill("Orange")
    sun.setOutline("red")

drawHouse()
drawSun()
win.getMouse()
win.close()
