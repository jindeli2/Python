import graphics as g

barwidth=400
barheight=150
numrec=16 #Sets the number of rectangles drawn 
wRect=barwidth/numrec #gets width of each rectangle
colorStep=255//numrec #gets the change of color for each step
win=g.GraphWin(width=barwidth,height=barheight, title='Gradient Bar')
green=0
x=0
for i in range(numrec):
    r=g.Rectangle(g.Point(x,0),g.Point(x+wRect,barheight))
    c="#%02x%02x%02x" % (70,green,0)
    r.setWidth(0)
    r.setFill(c)
    r.draw(win)
    green+=colorStep
    x+=(wRect)

win.getMouse()
win.close()