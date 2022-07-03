import math
import sys
import matplotlib.pyplot as plt



class Vertex:
    id = 0
    x = 0
    y = 0
    visited = False

    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id

def CalculateSinglePath(ver1, ver2):
    return math.sqrt(abs(ver1.x - ver2.x)**2 + abs(ver1.y - ver2.y)**2)

def CalculateSquence(startingPoint: int):

    f = open("coor.txt")
    line = f.readlines()
    xFromFile = line[0].split("/")
    xFromFile.pop()
    xFromFile = list(map(int, xFromFile))

    yFromFile = line[1].split("/")
    yFromFile.pop()
    yFromFile = list(map(int,yFromFile))
    f.close()

    minDistance = sys.maxsize * 2 + 1
    theNearestVertexId = 0
    orderOfVertexes = []
    xData = []
    yData = []
    vertexes = []

    vertexes.clear()

    temp = 0
    for x in xFromFile:
        vertexes.append(Vertex(x,yFromFile[temp],temp))
        temp = temp+1

    startVertex = vertexes[startingPoint]
    currentVertex = startVertex
    orderOfVertexes.append(vertexes[currentVertex.id])
    vertexes[startingPoint].visited = True
    
    for i in range(len(vertexes)-1):
        for j in vertexes:
            if (j.visited == True or j.id == currentVertex.id):
                continue
    
            currentDistance = CalculateSinglePath(currentVertex, j)
    
            if (currentDistance < minDistance):
                minDistance = currentDistance
                theNearestVertexId = j.id
            
        orderOfVertexes.append(vertexes[theNearestVertexId])
        currentVertex = vertexes[theNearestVertexId]
        vertexes[theNearestVertexId].visited = True
        minDistance = sys.maxsize * 2 + 1123
    
    orderOfVertexes.append(startVertex)
    
    for i in orderOfVertexes:
        xData.append(vertexes[i.id].x)
        yData.append(vertexes[i.id].y)

    finalDistance = 0
    for i in range(len(xData) - 1):
        pointA = [xData[i], yData[i]]
        pointB = [xData[i + 1], yData[i + 1]]
        distance = math.dist(pointA, pointB)
        finalDistance += distance
    lastPoint =[xData[len(xData) - 1], yData[len(xData) - 1]]
    firstPoint = [xData[0], yData[0]]
    lastDistance = math.dist(lastPoint, firstPoint)
    finalDistance += lastDistance


    plt.xlim(0,100)
    plt.ylim(0,100)
    
    plt.clf()
    plt.plot(xData, yData)
    plt.savefig('TNN.png')
    return finalDistance