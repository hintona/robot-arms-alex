import csv

def dataProcessor():

    data = []
    timeStamp = 0

    with open('RectangleDraw - Sheet12.csv','r')as firstFile:
        csvReader = csv.reader(firstFile)

        for line in csvReader:
            data.append(line[0])

    increment = 1/len(data)

    with open('WaistTogether.csv','w') as secondFile:
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