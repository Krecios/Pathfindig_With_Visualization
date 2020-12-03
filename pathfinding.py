import random

labirynth = []
startCoordinates = []
endCoordinates = []
wallCoordinates = []


def ReadLabirynth():
    file = open("labirinth.txt", "r")
    for line in file:
        labirynth.append(line[:-1])


def WhereIsStart():
    rowCounter = 0
    collumnCounter = 0
    for line in labirynth:
        for char in line:
            if char == "S":
                print("The start of the labirinth is a coordinates: X: " +
                      str(rowCounter) + " Y: " + str(collumnCounter))
                return [rowCounter, collumnCounter]
            rowCounter = rowCounter + 1
        rowCounter = 0
        collumnCounter = collumnCounter + 1


def WhereIsEnd():
    rowCounter = 0
    collumnCounter = 0
    for line in labirynth:
        for char in line:
            if char == "E":
                print("The end of the labirinth is a coordinates: X: " +
                      str(rowCounter) + " Y: " + str(collumnCounter))
                return [rowCounter, collumnCounter]
            rowCounter = rowCounter + 1
        rowCounter = 0
        collumnCounter = collumnCounter + 1


def WhereAreWalls():
    listOfWalls = []
    rowCounter = 0
    collumnCounter = 0
    for line in labirynth:
        for char in line:
            if char == "1":
                listOfWalls.append([rowCounter, collumnCounter])
            rowCounter = rowCounter + 1
        rowCounter = 0
        collumnCounter = collumnCounter + 1
    return listOfWalls


def IsCoordinateAWall(coordinate):
    for coord in wallCoordinates:
        if(coordinate == coord):
            return True
    return False


def RandomWalk():
    currentCoordinates = startCoordinates
    path = []
    while True:
        path.append(currentCoordinates)
        available = []
        availableCount = 0
        if currentCoordinates == endCoordinates:
            print("Exit found")
            print(path)
            return
        right = [currentCoordinates[0], currentCoordinates[1] + 1]
        left = [currentCoordinates[0], currentCoordinates[1] - 1]
        up = [currentCoordinates[0] - 1, currentCoordinates[1]]
        down = [currentCoordinates[0] + 1, currentCoordinates[1]]
        if IsCoordinateAWall(right) == False:
            available.append(right)
            availableCount = availableCount + 1
        if IsCoordinateAWall(left) == False:
            available.append(left)
            availableCount = availableCount + 1
        if IsCoordinateAWall(up) == False:
            available.append(up)
            availableCount = availableCount + 1
        if IsCoordinateAWall(down) == False:
            available.append(down)
            availableCount = availableCount + 1
        currentCoordinates = available[random.randint(0, availableCount - 1)]


ReadLabirynth()
startCoordinates = WhereIsStart()
endCoordinates = WhereIsEnd()
print(endCoordinates)
wallCoordinates = WhereAreWalls()
RandomWalk()
