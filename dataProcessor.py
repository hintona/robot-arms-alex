import csv

def dataProcessor():

    data = []
    timeStamp = 0

    with open('RectangleDraw - Trial10.csv','r')as firstFile:
        csvReader = csv.reader(firstFile)

        for line in csvReader:
            data.append(line[3])

    increment = 1/len(data)

    with open('processedWristAngle10.csv','w') as secondFile:
        csvWriter = csv.writer(secondFile)
        csvWriter.writerow(["time","position"])

        for item in data:
            strippedItem = str(item)
            strippedItem = strippedItem.replace("'","")
            strippedItem = strippedItem.replace("[","")
            strippedItem = strippedItem.replace("]","")
            newLine = [timeStamp,strippedItem]
            csvWriter.writerow(newLine)
            timeStamp = timeStamp + increment

dataProcessor()