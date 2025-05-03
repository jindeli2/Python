import random
  
def getShape(): 
    shapes = ["Rectangle", "Circle"]    
    return random.choice(shapes)

def randomXY(): 
    return random.randrange(1,500)

def randomColorBlue(): 
    return random.randrange(192,255)

def getColorRed(): 
    return 50

def getColorGreen(): 
    return 150

def getRGBColors(): 
    r = getColorRed()
    g = getColorGreen()
    b = randomColorBlue()
    rgb = r,g,b
    return rgb

def getStartCoord(): 
    stXPt = randomXY()
    stYPt = randomXY()
    return stXPt, stYPt

def getEndCoord(stXPt, stYPt): 
    endXPt = random.randrange(stXPt, 500) 
    endYPt = random.randrange(stYPt, 500)
    return endXPt, endYPt

def getRectangleShape(startingCoord, endingCoord): 
    startingCoord = coordniateStripperP(getStartCoord()) 
    stXPt,stYPt = map(int,startingCoord.split(','))   
    endingCoord = coordniateStripperP(getEndCoord(stXPt,stYPt)) 
    
    return startingCoord,endingCoord

def coordniateStripperP(x): 
    return str(x).strip('()')

def getCircleRadius(): 
    return random.randrange(5,50)

def main():
    outputFileName = input("Enter the drawing file name to create: ") #Gets file name.
    outFile = open(outputFileName, "w") 
    numOfShapes = int(input("Enter the number of shapes to make: ")) 
    for i in range(numOfShapes):  
        startingCoord = None 
        endingCoord = None
        circleRadius = None
        rgb = coordniateStripperP(getRGBColors()) 
        shape = getShape() 
        if shape == 'Rectangle': 
            startingCoord, endingCoord = getRectangleShape(startingCoord, endingCoord)
            print('{}; {}; {}; {}'.format(shape, startingCoord,endingCoord,rgb),file=outFile)
                    
        else:
            startingCoord = getStartCoord()
            startingCoord = coordniateStripperP(startingCoord)
            circleRadius = getCircleRadius()
            print('{}; {}; {}; {}'.format(shape, startingCoord,circleRadius,rgb),file=outFile)
        
    outFile.close() 

main()
