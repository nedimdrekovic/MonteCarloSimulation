
def setup():
    global circlePoints, squarePoints
    size(windowSize, windowSize * 9 / 8)
    background(193,225,236)
    
    if (n <= 0) | (n >= 4000000):
        textSize(20)
        print("jo")
        fill(255, 0, 0)
        text("For the value of n, choose a number in [1, 4.000.000)", 10, windowSize * 1 / 2)
        text("otherwise it takes too much time to execute the program.", 10, windowSize * 1 / 2 + 30)
        return

    # draw circle with radius of size of the window
    strokeWeight(.5)
    circle(windowSize/2, windowSize/2, windowSize)
    
    # set stroke settings for points
    stroke(255, 0, 0)
    if n < 50000:
        strokeWeight(3)
    elif n < 100000:
        strokeWeight(2)
    elif n < 1000000:
        strokeWeight(1)

    start = millis()    # starts counting time needed to draw all points
    for _ in range(n):
        # get x and y value
        x, y = spawnRandomCoords()        
        if ((x - windowSize/2)**2 + (y - windowSize/2)**2) < (windowSize/2)**2:
            circlePoints += 1
            stroke(0, 255, 0)
        else:
            stroke(255, 0, 0)
        squarePoints += 1

        point(x, y)        # draw point
    ending = millis()

    stroke(0)
    strokeWeight(4)
    line(0, windowSize, windowSize, windowSize)

    textSize(windowSize / 40)
    fill(0, 102, 153)
    s = str(n) if n < 1000 else (str(n/1000) + "." + str(n)[-3:]) if n < 1000000 else (str(n/1000000) + "." + str(n)[-6:-3] + "." + str(n)[-3:])     # format string
    text("value of pi after " + s + " iterations = "
         + str(round(calcPi(circlePoints, squarePoints), 5))
         + "  (~ " + str((ending-start)/1000) + "." 
         + str((ending-start)%1000)[:2]
         + " sec)",
         10,
         windowSize + windowSize * 1 / 16)    # output text string

    print(calcPi(circlePoints, squarePoints))    # prints more accurate current value of pi

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
    circleSize = 2 * windowSize    # diameter of the circle
    circlePoints = 0    # number of points in the circle
    squarePoints = 0    # number of points in the whole square including the circle    
    n = 20000    # number of iterations
