import csv

# Reads from 10 CSV files each with the same joint in it and averages it together
# Requires each CSV file to only contain numbers, and to be the same length. 
# Each CSV file should have lines in this format: time,position

def dataProcessor2():

    #read from each csv file
    #for the length of the first file, 
    #add togethr the values of item1 from each line of the csv file
    #and get av, print to ew file avg w timestamp
    time = []
    data1 = []
    data2 = []
    data3 = []
    data4 = []
    data5 = []
    data6 = []
    data7 = []
    data8 = []
    data9 = []
    data10 = []

    with open('wristangle/processedWristAngle1.csv','r')as file1:
        csvReader = csv.reader(file1)

        for line in csvReader:
            time.append(line[0])
            data1.append(line[1])

    with open('wristangle/processedWristAngle2.csv','r')as file2:
        csvReader = csv.reader(file2)

        for line in csvReader:
            data2.append(line[1])
    
    with open('wristangle/processedWristAngle3.csv','r')as file3:
        csvReader = csv.reader(file3)

        for line in csvReader:
            data3.append(line[1])

    with open('wristangle/processedWristAngle4.csv','r')as file4:
        csvReader = csv.reader(file4)

        for line in csvReader:
            data4.append(line[1])

    with open('wristangle/processedWristAngle5.csv','r')as file5:
        csvReader = csv.reader(file5)

        for line in csvReader:
            data5.append(line[1])

    with open('wristangle/processedWristAngle6.csv','r')as file6:
        csvReader = csv.reader(file6)

        for line in csvReader:
            data6.append(line[1])

    with open('wristangle/processedWristAngle7.csv','r')as file7:
        csvReader = csv.reader(file7)

        for line in csvReader:
            data7.append(line[1])
    
    with open('wristangle/processedWristAngle8.csv','r')as file8:
        csvReader = csv.reader(file8)

        for line in csvReader:
            data8.append(line[1])

    with open('wristangle/processedWristAngle9.csv','r')as file9:
        csvReader = csv.reader(file9)

        for line in csvReader:
            data9.append(line[1])

    with open('wristangle/processedWristAngle10.csv','r')as file10:
        csvReader = csv.reader(file10)

        for line in csvReader:
            data10.append(line[1])

    length = len(time)

    with open('wristAngleAvg.csv','w') as endFile:
        csvWriter = csv.writer(endFile)
        csvWriter.writerow(["time","average position"]) 

        for num in range(length):
            sum = float(data1[num]) + float(data2[num]) + float(data3[num]) + float(data4[num]) + float(data5[num]) + float(data6[num]) + float(data7[num]) + float(data8[num]) + float(data9[num]) + float(data10[num])
            avg = sum / 10
            timeStamp = time[num]
            csvWriter.writerow([timeStamp,avg])

dataProcessor2()