
def setup():
    global circlePoints, squarePoints
    size(windowSize, windowSize * 9 / 8)
    background(250)
    
    # draw circle with radius of size of the window
    strokeWeight(.5)
    fill(250)
    circle(windowSize/2, windowSize/2, circleDiameter)
    
def draw():
    global circlePoints, squarePoints, n
    #background(193,225,236)
    if (n < 0):
        textSize(20)
        fill(255, 0, 0)
        text("For the value of n, choose a number > 0", 10, windowSize * 1 / 2)
        return

    # set stroke settings for points
    stroke(255, 0, 0)
    strokeWeight(1)

    for _ in range(100):
        # get x and y value
        x, y = spawnRandomCoords()        
        if ((x - windowSize/2)**2 + (y - windowSize/2)**2) < (windowSize/2)**2:
            circlePoints += 1    # increase number of points that are in the circle
            stroke(0, 255, 0)
        else:
            stroke(255, 0, 0)
        squarePoints += 1    # points in the square
        n += 1

        point(x, y)        # draw point

    stroke(0)
    strokeWeight(.5)
    fill(193,225,236)
    rect(0, windowSize, windowSize, windowSize - windowSize * 1 / 8)

    textSize(windowSize / 40)
    fill(0, 102, 153)
    s = str(n) if n < 1000 else (str(n/1000) + "." + str(n)[-3:]) if n < 1000000 else (str(n/1000000) + "." + str(n)[-6:-3] + "." + str(n)[-3:])     # format string
    text("Value of pi after " + s + " iterations = "
         + str(round(calcPi(circlePoints, squarePoints), decimalPlaces)),
         10,
         windowSize + windowSize * 1 / 16)    # output text string

def calcPi(points_circle, points_square):
    '''
    Calculate and approximate current value of pi
    '''
    pi = float(points_circle) / float(points_square)
    return 4.0 * pi

def spawnRandomCoords():
    '''
    Generates x and y coords of new points if it is
    not already generated and returns it.
    '''
    return random(windowSize), random(windowSize)

if __name__ == '__main__':
    windowSize = 500    # size of the window
    circleDiameter = windowSize    # diameter of circle
    circlePoints = 0    # number of points in the circle
    squarePoints = 0    # number of points in the whole square including the circle    
    n = 0    # number of iterations
    decimalPlaces = 8    # number of digits after decimal point
    
