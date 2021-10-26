import csv

def dataProcessor():

    data = []
    timeStamp = 0

    with open('data - Sheet1.csv','r')as firstFile:
        csvReader = csv.reader(firstFile)

        for line in csvReader:
            data.append(line)

    increment = 1/len(data)

    with open('processedWristRotate5.csv','w') as secondFile:
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