import csv
import matplotlib.pyplot as plt
import numpy as np

def graphData():
    xData1 = []
    yData1 = []

    with open('shoulder/processedShoulder1.csv','r')as firstFile:
        csvReader = csv.reader(firstFile)

        for line in csvReader:
            xData1.append(line[0])
            yData1.append(line[1])

    xData2 = []
    yData2 = []
    
    with open('shoulder/processedShoulder2.csv','r')as firstFile:
        csvReader = csv.reader(firstFile)

        for line in csvReader:
            xData2.append(line[0])
            yData2.append(line[1])

    xData3 = []
    yData3 = []
    
    with open('shoulder/processedShoulder3.csv','r')as firstFile:
        csvReader = csv.reader(firstFile)

        for line in csvReader:
            xData3.append(line[0])
            yData3.append(line[1])

    xData4 = []
    yData4 = []
    
    with open('shoulder/processedShoulder4.csv','r')as firstFile:
        csvReader = csv.reader(firstFile)

        for line in csvReader:
            xData4.append(line[0])
            yData4.append(line[1])

    xData5 = []
    yData5 = []
    
    with open('shoulder/processedShoulder5.csv','r')as firstFile:
        csvReader = csv.reader(firstFile)

        for line in csvReader:
            xData5.append(line[0])
            yData5.append(line[1])

    plt.rcParams["figure.figsize"] = [20, 10]
    plt.rcParams["figure.autolayout"] = True
    plt.plot(xData1,yData1)
    plt.plot(xData2,yData2)
    plt.plot(xData3,yData3)
    plt.plot(xData4,yData4)
    plt.plot(xData5,yData5)
    plt.show()

graphData()