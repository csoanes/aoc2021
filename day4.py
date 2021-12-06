import numpy as np
from pprint import pprint


path = '/Users/root1/AoC2021Data/Day4/day4Cards.txt'
path2 = '/Users/root1/AoC2021Data/Day4/day4Numbers.txt'

def check_bingo():
    winningIndex = 0
    winningIndices=[]
    for np_card in np_cards:
        print("Cards remaining: ", np_cards.shape)
        pprint(np_card)
        #sum all the rows
        sumRows = np_card.sum(axis=0)
        sumColumns = +np_card.sum(axis=1)
        #pprint (sumRows)
        #pprint (sumColumns)
        if np.in1d(-5, sumRows) | np.in1d(-5, sumColumns):
            winningIndices.append(winningIndex)
        else:
            winningIndex+=1
    return winningIndices


with open(path) as file:
    lines = file.readlines()
    print("Lines:", lines)
    cardNum = 0
    rowNum = 0
    cards = []
    for line in lines:
        line=line.rstrip()
        #print ("Examining line: ",line)
        if not line:
            cardNum += 1
            rowNum = 0
            cards.append(rows)
        else:
            if rowNum == 0:
                rows = []
            bingoStringArr = line.split()
            #print("BingoStringArr: ", bingoStringArr);
            bingoNumArr = [int(numeric_string) for numeric_string in bingoStringArr]
            #print("BingoNumArr: ", bingoNumArr)
            rows.append(bingoNumArr)
            rowNum += 1
            if rowNum > 5:
                cards.append(rows)

    print("Cards: ")

    np_cards = np.array(cards)
    pprint (np_cards)

with open(path2) as file2:
    line = file2.readline()
    print(line)
    callsStrArr = line.split(',')
    callsArr = [int(numeric_string) for numeric_string in callsStrArr]
    print(callsArr)
    winningSums = []
    for call in callsArr:
        print ("Call:", call)
        np_cards = np.where(np_cards ==call, -1, np_cards)
        winningIndices = check_bingo()
        print("WinningIndices: ", winningIndices)
        if winningIndices:
            print("House!")
            for winningIndex in winningIndices:
                print("card:", winningIndex)
                winningCard = np.copy(np_cards[winningIndex])
                #pprint(winningCard)
                winningCard = np.where(winningCard == -1, 0, winningCard)
                #pprint(winningCard)
                print (call)
                print (winningCard.sum())
                print ("Sum of winnong card * call: ", call*winningCard.sum())
                winningSums.append(call*winningCard.sum())
                np_cards = np.delete(np_cards, winningIndex, 0)

print(winningSums)