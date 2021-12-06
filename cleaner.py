# Purpose is to remove the flat lines at the start and stop of each joint 
# so we can fit lines better
# This will run on 20 individual CSV files that each contain raw data for 
# all joints on the robot
# This will return a single CSV file for a single joint that contains each
# trial for that joint, all normalised, and with the flat ends trimmed off
# The user will need to pass in which joint they want trimmed, what value
# the flat end that they want trimmed is, and whether the program should 
# remove values above, below, or at the given value.
import csv


def cleaner():

    # jointNum should be given the number that corresponds with which joint you
    # want cleaned up. Below are the values that correspond with each joint
    # waist = 0
    # shoulder = 1
    # elbow = 2
    # wrist_angle = 3
    # wrist_rotate = 4
    # gripper = 5
    # left_finger = 6
    # right_finger = 7
    jointNum = 3

    # This should be given the value of the flat segments at the start and end of the 
    # file that you want trimmed off. 
    flatline = 0.632

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
    data11 = []
    data12 = []
    data13 = []
    data14 = []
    data15 = []
    data16 = []
    data17 = []
    data18 = []
    data19 = []
    data20 = []


    #reads each file into an array
    with open('Raw X-Data/JointStates1.csv','r')as file1:
        csvReader = csv.reader(file1)

        for line in csvReader:
            data1.append(line[jointNum])

    with open('Raw X-Data/JointStates2.csv','r')as file2:
        csvReader = csv.reader(file2)

        for line in csvReader:
            data2.append(line[jointNum])

    with open('Raw X-Data/JointStates3.csv','r')as file3:
        csvReader = csv.reader(file3)

        for line in csvReader:
            data3.append(line[jointNum])

    with open('Raw X-Data/JointStates4.csv','r')as file4:
        csvReader = csv.reader(file4)

        for line in csvReader:
            data4.append(line[jointNum])

    with open('Raw X-Data/JointStates5.csv','r')as file5:
        csvReader = csv.reader(file5)

        for line in csvReader:
            data5.append(line[jointNum])

    with open('Raw X-Data/JointStates6.csv','r')as file6:
        csvReader = csv.reader(file6)

        for line in csvReader:
            data6.append(line[jointNum])

    with open('Raw X-Data/JointStates7.csv','r')as file7:
        csvReader = csv.reader(file7)

        for line in csvReader:
            data7.append(line[jointNum])

    with open('Raw X-Data/JointStates8.csv','r')as file8:
        csvReader = csv.reader(file8)

        for line in csvReader:
            data8.append(line[jointNum])

    with open('Raw X-Data/JointStates9.csv','r')as file9:
        csvReader = csv.reader(file9)

        for line in csvReader:
            data9.append(line[jointNum])

    with open('Raw X-Data/JointStates10.csv','r')as file10:
        csvReader = csv.reader(file10)

        for line in csvReader:
            data10.append(line[jointNum])

    with open('Raw X-Data/JointStates11.csv','r')as file11:
        csvReader = csv.reader(file11)

        for line in csvReader:
            data11.append(line[jointNum])

    with open('Raw X-Data/JointStates12.csv','r')as file12:
        csvReader = csv.reader(file12)

        for line in csvReader:
            data12.append(line[jointNum])

    with open('Raw X-Data/JointStates13.csv','r')as file13:
        csvReader = csv.reader(file13)

        for line in csvReader:
            data13.append(line[jointNum])

    with open('Raw X-Data/JointStates14.csv','r')as file14:
        csvReader = csv.reader(file14)

        for line in csvReader:
            data14.append(line[jointNum])

    with open('Raw X-Data/JointStates15.csv','r')as file15:
        csvReader = csv.reader(file15)

        for line in csvReader:
            data15.append(line[jointNum])

    with open('Raw X-Data/JointStates16.csv','r')as file16:
        csvReader = csv.reader(file16)

        for line in csvReader:
            data16.append(line[jointNum])

    with open('Raw X-Data/JointStates17.csv','r')as file17:
        csvReader = csv.reader(file17)

        for line in csvReader:
            data17.append(line[jointNum])

    with open('Raw X-Data/JointStates18.csv','r')as file18:
        csvReader = csv.reader(file18)

        for line in csvReader:
            data18.append(line[jointNum])

    with open('Raw X-Data/JointStates19.csv','r')as file19:
        csvReader = csv.reader(file19)

        for line in csvReader:
            data19.append(line[jointNum])

    with open('Raw X-Data/JointStates20.csv','r')as file20:
        csvReader = csv.reader(file20)

        for line in csvReader:
            data20.append(line[jointNum])



    #loop thru array to remove everything that is at that particular joint's flatline
    # At this point, the user should change the operator in line 181 to adjust if the 
    # program should remove values above, below, or at the given value
    temp = []
    for item in data1:
        if float(item) < flatline:
            temp.append(item)
    data1 = temp
    temp = []

    for item in data2:
        if float(item) < flatline:
            temp.append(item)
    data2 = temp
    temp = []

    for item in data3:
        if float(item) < flatline:
            temp.append(item)
    data3 = temp
    temp = []

    for item in data4:
        if float(item) < flatline:
            temp.append(item)
    data4 = temp
    temp = []

    for item in data5:
        if float(item) < flatline:
            temp.append(item)
    data5 = temp
    temp = []

    for item in data6:
        if float(item) < flatline:
            temp.append(item)
    data6 = temp
    temp = []

    for item in data7:
        if float(item) < flatline:
            temp.append(item)
    data7 = temp
    temp = []

    for item in data8:
        if float(item) < flatline:
            temp.append(item)
    data8 = temp
    temp = []

    for item in data9:
        if float(item) < flatline:
            temp.append(item)
    data9 = temp
    temp = []

    for item in data10:
        if float(item) < flatline:
            temp.append(item)
    data10 = temp
    temp = []

    for item in data11:
        if float(item) < flatline:
            temp.append(item)
    data11 = temp
    temp = []

    for item in data12:
        if float(item) < flatline:
            temp.append(item)
    data12 = temp
    temp = []

    for item in data13:
        if float(item) < flatline:
            temp.append(item)
    data13 = temp
    temp = []

    for item in data14:
        if float(item) < flatline:
            temp.append(item)
    data14 = temp
    temp = []

    for item in data15:
        if float(item) < flatline:
            temp.append(item)
    data15 = temp
    temp = []

    for item in data16:
        if float(item) < flatline:
            temp.append(item)
    data16 = temp
    temp = []

    for item in data17:
        if float(item) < flatline:
            temp.append(item)
    data17 = temp
    temp = []

    for item in data18:
        if float(item) < flatline:
            temp.append(item)
    data18 = temp
    temp = []

    for item in data19:
        if float(item) < flatline:
            temp.append(item)
    data19 = temp
    temp = []

    for item in data20:
        if float(item) < flatline:
            temp.append(item)
    data20 = temp
    temp = []
    

    # Normalises each trial now that the flat lines have been removed. 
    with open('WaistTogether.csv','w') as outputFile:
        csvWriter = csv.writer(outputFile)
        csvWriter.writerow(["time","position"])

        timeStamp = 0
        increment = 1/len(data1)

        for item in data1:
            strippedItem = str(item)
            strippedItem = strippedItem.replace("'","")
            strippedItem = strippedItem.replace("[","")
            strippedItem = strippedItem.replace("]","")
            newLine = [timeStamp,strippedItem]
            csvWriter.writerow(newLine)
            timeStamp = timeStamp + increment

        timeStamp = 0
        increment = 1/len(data2)

        for item in data2:
            strippedItem = str(item)
            strippedItem = strippedItem.replace("'","")
            strippedItem = strippedItem.replace("[","")
            strippedItem = strippedItem.replace("]","")
            newLine = [timeStamp,strippedItem]
            csvWriter.writerow(newLine)
            timeStamp = timeStamp + increment

        timeStamp = 0
        increment = 1/len(data3)

        for item in data3:
            strippedItem = str(item)
            strippedItem = strippedItem.replace("'","")
            strippedItem = strippedItem.replace("[","")
            strippedItem = strippedItem.replace("]","")
            newLine = [timeStamp,strippedItem]
            csvWriter.writerow(newLine)
            timeStamp = timeStamp + increment

        timeStamp = 0
        increment = 1/len(data4)

        for item in data4:
            strippedItem = str(item)
            strippedItem = strippedItem.replace("'","")
            strippedItem = strippedItem.replace("[","")
            strippedItem = strippedItem.replace("]","")
            newLine = [timeStamp,strippedItem]
            csvWriter.writerow(newLine)
            timeStamp = timeStamp + increment

        timeStamp = 0
        increment = 1/len(data5)

        for item in data5:
            strippedItem = str(item)
            strippedItem = strippedItem.replace("'","")
            strippedItem = strippedItem.replace("[","")
            strippedItem = strippedItem.replace("]","")
            newLine = [timeStamp,strippedItem]
            csvWriter.writerow(newLine)
            timeStamp = timeStamp + increment

        timeStamp = 0
        increment = 1/len(data6)

        for item in data6:
            strippedItem = str(item)
            strippedItem = strippedItem.replace("'","")
            strippedItem = strippedItem.replace("[","")
            strippedItem = strippedItem.replace("]","")
            newLine = [timeStamp,strippedItem]
            csvWriter.writerow(newLine)
            timeStamp = timeStamp + increment

        timeStamp = 0
        increment = 1/len(data7)

        for item in data7:
            strippedItem = str(item)
            strippedItem = strippedItem.replace("'","")
            strippedItem = strippedItem.replace("[","")
            strippedItem = strippedItem.replace("]","")
            newLine = [timeStamp,strippedItem]
            csvWriter.writerow(newLine)
            timeStamp = timeStamp + increment

        timeStamp = 0
        increment = 1/len(data8)

        for item in data8:
            strippedItem = str(item)
            strippedItem = strippedItem.replace("'","")
            strippedItem = strippedItem.replace("[","")
            strippedItem = strippedItem.replace("]","")
            newLine = [timeStamp,strippedItem]
            csvWriter.writerow(newLine)
            timeStamp = timeStamp + increment

        timeStamp = 0
        increment = 1/len(data9)

        for item in data9:
            strippedItem = str(item)
            strippedItem = strippedItem.replace("'","")
            strippedItem = strippedItem.replace("[","")
            strippedItem = strippedItem.replace("]","")
            newLine = [timeStamp,strippedItem]
            csvWriter.writerow(newLine)
            timeStamp = timeStamp + increment

        timeStamp = 0
        increment = 1/len(data10)

        for item in data10:
            strippedItem = str(item)
            strippedItem = strippedItem.replace("'","")
            strippedItem = strippedItem.replace("[","")
            strippedItem = strippedItem.replace("]","")
            newLine = [timeStamp,strippedItem]
            csvWriter.writerow(newLine)
            timeStamp = timeStamp + increment

        timeStamp = 0
        increment = 1/len(data11)

        for item in data11:
            strippedItem = str(item)
            strippedItem = strippedItem.replace("'","")
            strippedItem = strippedItem.replace("[","")
            strippedItem = strippedItem.replace("]","")
            newLine = [timeStamp,strippedItem]
            csvWriter.writerow(newLine)
            timeStamp = timeStamp + increment

        timeStamp = 0
        increment = 1/len(data12)

        for item in data12:
            strippedItem = str(item)
            strippedItem = strippedItem.replace("'","")
            strippedItem = strippedItem.replace("[","")
            strippedItem = strippedItem.replace("]","")
            newLine = [timeStamp,strippedItem]
            csvWriter.writerow(newLine)
            timeStamp = timeStamp + increment

        timeStamp = 0
        increment = 1/len(data13)

        for item in data13:
            strippedItem = str(item)
            strippedItem = strippedItem.replace("'","")
            strippedItem = strippedItem.replace("[","")
            strippedItem = strippedItem.replace("]","")
            newLine = [timeStamp,strippedItem]
            csvWriter.writerow(newLine)
            timeStamp = timeStamp + increment

        timeStamp = 0
        increment = 1/len(data14)

        for item in data14:
            strippedItem = str(item)
            strippedItem = strippedItem.replace("'","")
            strippedItem = strippedItem.replace("[","")
            strippedItem = strippedItem.replace("]","")
            newLine = [timeStamp,strippedItem]
            csvWriter.writerow(newLine)
            timeStamp = timeStamp + increment

        timeStamp = 0
        increment = 1/len(data15)

        for item in data15:
            strippedItem = str(item)
            strippedItem = strippedItem.replace("'","")
            strippedItem = strippedItem.replace("[","")
            strippedItem = strippedItem.replace("]","")
            newLine = [timeStamp,strippedItem]
            csvWriter.writerow(newLine)
            timeStamp = timeStamp + increment

        timeStamp = 0
        increment = 1/len(data16)

        for item in data16:
            strippedItem = str(item)
            strippedItem = strippedItem.replace("'","")
            strippedItem = strippedItem.replace("[","")
            strippedItem = strippedItem.replace("]","")
            newLine = [timeStamp,strippedItem]
            csvWriter.writerow(newLine)
            timeStamp = timeStamp + increment

        timeStamp = 0
        increment = 1/len(data17)

        for item in data17:
            strippedItem = str(item)
            strippedItem = strippedItem.replace("'","")
            strippedItem = strippedItem.replace("[","")
            strippedItem = strippedItem.replace("]","")
            newLine = [timeStamp,strippedItem]
            csvWriter.writerow(newLine)
            timeStamp = timeStamp + increment

        timeStamp = 0
        increment = 1/len(data18)

        for item in data18:
            strippedItem = str(item)
            strippedItem = strippedItem.replace("'","")
            strippedItem = strippedItem.replace("[","")
            strippedItem = strippedItem.replace("]","")
            newLine = [timeStamp,strippedItem]
            csvWriter.writerow(newLine)
            timeStamp = timeStamp + increment

        timeStamp = 0
        increment = 1/len(data19)

        for item in data19:
            strippedItem = str(item)
            strippedItem = strippedItem.replace("'","")
            strippedItem = strippedItem.replace("[","")
            strippedItem = strippedItem.replace("]","")
            newLine = [timeStamp,strippedItem]
            csvWriter.writerow(newLine)
            timeStamp = timeStamp + increment

        timeStamp = 0
        increment = 1/len(data20)

        for item in data20:
            strippedItem = str(item)
            strippedItem = strippedItem.replace("'","")
            strippedItem = strippedItem.replace("[","")
            strippedItem = strippedItem.replace("]","")
            newLine = [timeStamp,strippedItem]
            csvWriter.writerow(newLine)
            timeStamp = timeStamp + increment




cleaner()