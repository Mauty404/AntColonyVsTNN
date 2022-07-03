import math
import numpy as np
from matplotlib import pyplot as plt

from ant_colony import AntColony

def CalculateAntColony(numOfAnts, numOfIterations):
    f = open("coor.txt")
    line = f.readlines()
    xFromFile = line[0].split("/")
    xFromFile.pop()
    xFromFile = list(map(int, xFromFile))

    yFromFile = line[1].split("/")
    yFromFile.pop()
    yFromFile = list(map(int, yFromFile))
    f.close()

    distancesList = []

    for i in range(len(xFromFile)):
        distancesList.append([])
        for j in range(len(xFromFile)):
            if i == j:
                distancesList[i].append(np.inf)
                continue
            pointA = [xFromFile[i], yFromFile[i]]
            pointB = [xFromFile[j], yFromFile[j]]
            distance = math.dist(pointA, pointB)
            distancesList[i].append(distance)

    distances = np.array(distancesList)

    ant_colony = AntColony(distances, int(numOfAnts), 2, int(numOfIterations), 0.95, alpha=1, beta=1)
    final_distance, path = ant_colony.run()

    finalX = []
    finalY = []

    for i in range(len(xFromFile)):
        finalX.append(xFromFile[path[i][0]])
        finalY.append(yFromFile[path[i][0]])
    finalX.append(xFromFile[path[0][0]])
    finalY.append(yFromFile[path[0][0]])

    plt.xlim(0, 100)
    plt.ylim(0, 100)

    plt.clf()
    plt.plot(finalX, finalY)
    plt.savefig('AntColony.png')

    print(finalX)
    print(finalY)
    print(final_distance)
    return final_distance
