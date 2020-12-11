import random
import pygame
import sys
import time

pygame.display.set_caption("Pathfinding")
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
purple = (128, 0, 128)
orange = (255, 165, 0)
grey = (128, 128, 128)
turqoise = (64, 224, 208)

labirynth = []
startCoordinates = []
endCoordinates = []
wallCoordinates = []
visitedCoordinates = []
wholePath = []
rowCount = 0
collumnCount = 0


class Node:
    def __init__(self, row, collumn, width, totalRows):
        self.row = row
        self.collumn = collumn
        self.x = row * width
        self.y = collumn * width
        self.color = white
        self.neighbors = []
        self.width = width
        self.totalRows = totalRows

    def getPosition(self):
        return self.row, self.collumn

    def isVisited(self):
        return self.color == red

    def isAvailable(self):
        return self.color == green

    def isPresent(self):
        return self.color == black

    def isStart(self):
        return self.color == orange

    def isEnd(self):
        return self.color == turqoise

    def isPath(self):
        return self.color == purple

    def reset(self):
        return self.color == white

    def makeVisited(self):
        self.color = red

    def makeAvailable(self):
        self.color = green

    def makeWall(self):
        self.color = black

    def makeStart(self):
        self.color = orange

    def makeEnd(self):
        self.color = turqoise

    def makePath(self):
        self.color = purple

    def makeReset(self):
        self.color = white

    def draw(self, win):
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.width, self.width))


def makeGrid(rows, collumns, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(collumns):
            node = Node(i, j, gap, rows)
            if isPresent([i, j], wallCoordinates):
                node.makeWall()
            elif [i, j] == startCoordinates:
                node.makeStart()
            elif [i, j] == endCoordinates:
                node.makeEnd()
            elif isPresent([i, j], wholePath):
                node.makeVisited()
            grid[i].append(node)
    return grid


def drawGrid(win, rows, collumns, width):
    gap = width // rows
    for i in range(collumns):
        pygame.draw.line(win, grey, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, grey, (j * gap, 0), (j * gap, width))


def draw(win, grid, rows, collumns, width):
    win.fill(white)
    for row in grid:
        for node in row:
            node.draw(win)
    drawGrid(win, rows, collumns, width)
    pygame.display.update()


def readLabyrinth(filename):
    file = open(filename, "r")
    for line in file:
        if line[:-1] == '0' or line[:-1] == 1:
            labirynth.append(line)
        else:
            labirynth.append(line[:-1])
    rowCount = len(labirynth[0])
    collumnCount = len(labirynth)
    print("Rows : " + str(rowCount) + ", Collumns: " + str(collumnCount))
    return rowCount, collumnCount


def findStart():
    rowCounter = 0
    collumnCounter = 0
    for line in labirynth:
        for char in line:
            if char == "S":
                print("The start of the labyrinth is a coordinates: X: " +
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
                print("The end of the labyrinth is a coordinates: X: " +
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


def isPresent(coordinate, array):
    for coord in array:
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
    for y in range(rowCount - 1):
        for x in range(collumnCount + 1):
            if [x, y] == startCoordinates:
                file.write("S")
            elif [x, y] == endCoordinates:
                file.write("E")
            elif isPresent([x, y], wallCoordinates) == True:
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
        if isPresent(right, wallCoordinates) == False and isVisited(visitedCoordinates, right) == False and right != startCoordinates:
            available.append(right)
            availableCount = availableCount + 1
        if isPresent(left, wallCoordinates) == False and isVisited(visitedCoordinates, left) == False and left != startCoordinates:
            available.append(left)
            availableCount = availableCount + 1
        if isPresent(up, wallCoordinates) == False and isVisited(visitedCoordinates, up) == False and up != startCoordinates:
            available.append(up)
            availableCount = availableCount + 1
        if isPresent(down, wallCoordinates) == False and isVisited(visitedCoordinates, down) == False and down != startCoordinates:
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


rowCount, collumnCount = readLabyrinth('labyrinth.txt')
startCoordinates = findStart()
endCoordinates = findEnd()
wallCoordinates = findWalls()
width = 1000
window = pygame.display.set_mode((width, collumnCount * (width // rowCount)))
grid = makeGrid(rowCount, collumnCount, width)
wholePath = randomWalk()
if(wholePath != -1):
    drawSolution()
run = True
while run:
    draw(window, grid, rowCount, collumnCount, width)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                grid = makeGrid(rowCount, collumnCount, width)
pygame.quit()
