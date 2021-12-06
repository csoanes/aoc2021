
import numpy as np


path = '/Users/root1/AoC2021Data/Day3/day3Input.txt'


with open(path) as file:
    diagnostic = []
    while line := file.readline().rstrip():
        diagnostic.append(list(line))

    diagNum = np.array(diagnostic).astype(int)


    row = diagNum[:, 0]


    length = len(diagNum[0]);
    gamma = 0
    epsilon = 0
    for column in range(length):
        columnArr = diagNum[:, column]
        print(columnArr)
        # count the number of 1s and devide by len
        isGreater = (columnArr > 0).sum()
        if (round(isGreater / np.prod(columnArr.shape))) == 1:
            gamma += 2 ** ((length - 1) - column)
        else:
            epsilon += 2 ** ((length - 1) - column)
    print (gamma)
    print (epsilon)
    oxygenRating = np.copy(diagNum);
    print ("OxygenRating start: ", oxygenRating)
    for column in range(length):
        if len(oxygenRating[:,0]) == 1: break
        columnArr = oxygenRating[:, column]
        print("ColumnArr: ", columnArr)
        print("KeepOnes: ", (columnArr > 0).sum() > len(columnArr)/2)
        if (columnArr > 0).sum() >= (len(columnArr)/2):
            print("Deleting all rows where column : ", column, " contains 0")
            oxygenRating=oxygenRating[oxygenRating[:, column] != 0]
            print(oxygenRating)
        else:
            print("Deleting all rows where column : ", column, " contains 1");
            oxygenRating=oxygenRating[oxygenRating[:, column] != 1]
            print(oxygenRating)

    print("OxygenRating end: ", oxygenRating)
    exp = len(oxygenRating[0])-1
    oxygen =0

    for num in oxygenRating[0]:
        if num ==1:
            oxygen += (2**exp)
        exp -=1

    co2Scrubber = np.copy(diagNum);
    print("co2Scrubber start: ", co2Scrubber)
    for column2 in range(length):
        if len(co2Scrubber[:, 0]) == 1: break
        columnArr = co2Scrubber[:, column2]
        print("ColumnArr: ", columnArr)
        print("KeepOnes: ", (columnArr > 0).sum() > len(columnArr) / 2)
        if (columnArr > 0).sum() >= (len(columnArr) / 2):
            print("Deleting all rows where column : ", column2, " contains 0")
            co2Scrubber = co2Scrubber[co2Scrubber[:, column2] != 1]
            print(co2Scrubber)
        else:
            print("Deleting all rows where column : ", column2, " contains 1");
            co2Scrubber = co2Scrubber[co2Scrubber[:, column2] != 0]
            print(co2Scrubber)

    print("co2Scrubber end: ", co2Scrubber)
    exp = len(co2Scrubber[0]) - 1
    co2 = 0

    for num2 in co2Scrubber[0]:
        if num2 == 1:
            co2 += (2 ** exp)
        exp -= 1

    print ("Power Comsumption: ", gamma * epsilon)
    print ("Oxygen Rating: ", oxygen)
    print ("Co2 Scrubber Rating: ", co2)
    print ("Life Support Raing: ", oxygen*co2)

