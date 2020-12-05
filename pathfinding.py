import random

labirynth = []
startCoordinates = []
endCoordinates = []
wallCoordinates = []
visitedCoordinates = []
wholePath = []
rowCount = 0
collumnCount = 0


def readLabirinth():
    file = open("labirinth.txt", "r")
    for line in file:
        labirynth.append(line[:-1])


def getDimensions():
    rowCount = len(labirynth[0])
    collumnCount = len(labirynth)
    print("Rows : " + str(rowCount) + ", Collumns: " + str(collumnCount))


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


def isVisited(currentPath, analyzedCoords):
    for coord in currentPath:
        if coord == analyzedCoords:
            return True
    return False


def checkSolution(path):
    for coord in path:
        counter = 0
        for coordCheck in path:
            if coord == coordCheck:
                counter = counter + 1
            if counter > 1:
                print("ERROR")
                return
    print("Correct")


def drawSolution():
    file = open("output.txt", "w")
    for y in range(12):
        for x in range(24):
            if [x, y] == startCoordinates:
                file.write("S")
            elif [x, y] == endCoordinates:
                file.write("E")
            elif isWall([x, y]) == True:
                file.write("1")
            elif isVisited(wholePath, [x, y]) == True:
                file.write("V")
            else:
                file.write("0")
        file.write("\n")


def randomWalk():
    currentCoordinates = startCoordinates
    path = []
    while True:
        available = []
        availableCount = 0
        if currentCoordinates == endCoordinates:
            print("Path found:")
            print(visitedCoordinates)
            checkSolution(visitedCoordinates)
            return visitedCoordinates
        right = [currentCoordinates[0], currentCoordinates[1] + 1]
        left = [currentCoordinates[0], currentCoordinates[1] - 1]
        up = [currentCoordinates[0] - 1, currentCoordinates[1]]
        down = [currentCoordinates[0] + 1, currentCoordinates[1]]
        if isWall(right) == False and isVisited(visitedCoordinates, right) == False and right != startCoordinates:
            available.append(right)
            availableCount = availableCount + 1
        if isWall(left) == False and isVisited(visitedCoordinates, left) == False and left != startCoordinates:
            available.append(left)
            availableCount = availableCount + 1
        if isWall(up) == False and isVisited(visitedCoordinates, up) == False and up != startCoordinates:
            available.append(up)
            availableCount = availableCount + 1
        if isWall(down) == False and isVisited(visitedCoordinates, down) == False and down != startCoordinates:
            available.append(down)
            availableCount = availableCount + 1
        if availableCount == 0:
            if(len(path) == 0):
                print('No solution')
                return -1
            currentCoordinates = path.pop()
            #print('Current coords: ', currentCoordinates)
            continue
        currentCoordinates = available[random.randint(0, availableCount - 1)]
        #print('Current coords: ', currentCoordinates)
        visitedCoordinates.append(currentCoordinates)
        path.append(currentCoordinates)


readLabirinth()
getDimensions()
startCoordinates = findStart()
endCoordinates = findEnd()
wallCoordinates = findWalls()
wholePath = randomWalk()
if(wholePath != -1):
    drawSolution()
