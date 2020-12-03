import random

labirynth = []
startCoordinates = []
endCoordinates = []
wallCoordinates = []


def readLab():
    file = open("labirinth.txt", "r")
    for line in file:
        labirynth.append(line[:-1])


def findStart():
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


def findEnd():
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


def findWalls():
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


def isWall(coordinate):
    for coord in wallCoordinates:
        if(coordinate == coord):
            return True
    return False


def randomWalk():
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
        if isWall(right) == False:
            available.append(right)
            availableCount = availableCount + 1
        if isWall(left) == False:
            available.append(left)
            availableCount = availableCount + 1
        if isWall(up) == False:
            available.append(up)
            availableCount = availableCount + 1
        if isWall(down) == False:
            available.append(down)
            availableCount = availableCount + 1
        currentCoordinates = available[random.randint(0, availableCount - 1)]


readLab()
startCoordinates = findStart()
endCoordinates = findEnd()
print(endCoordinates)
wallCoordinates = findWalls()
randomWalk()
