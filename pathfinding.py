labirynth = []
startCoordinates = []
endCoordinates = []
wallCoordinates = []


def readLabirynth():
    file = open("labirinth.txt", "r")
    for line in file:
        labirynth.append(line[:-1])


def whereIsStart():
    rowCounter = 0
    collumnCounter = 0
    for line in labirynth:
        for char in line:
            if char == "S":
                print("The start of the labirinth is a coordinates: X: " +
                      str(rowCounter) + " Y: " + str(collumnCounter))
                return (rowCounter, collumnCounter)
            rowCounter = rowCounter + 1
        rowCounter = 0
        collumnCounter = collumnCounter + 1


def whereIsEnd():
    rowCounter = 0
    collumnCounter = 0
    for line in labirynth:
        for char in line:
            if char == "E":
                print("The end of the labirinth is a coordinates: X: " +
                      str(rowCounter) + " Y: " + str(collumnCounter))
                return (rowCounter, collumnCounter)
            rowCounter = rowCounter + 1
        rowCounter = 0
        collumnCounter = collumnCounter + 1


def whereAreWalls():
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
    print(listOfWalls)
    return listOfWalls


readLabirynth()
startCoordinates = whereIsStart()
endCoordinates = whereIsEnd()
wallCoordinates = whereAreWalls()
