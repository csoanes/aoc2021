import numpy as np
from pprint import pprint

path = '/Users/root1/AoC2021Data/Day5/day5Data.txt'

def fullrange(start, end):
    if start > end:
        #counting backwards
        return (range(start,end-1,-1))
    else:
        return (range(start,end+1))

#tests of range
print(*fullrange(0,1))
print(*fullrange(1,0))
print(*fullrange(2,6))
print(*fullrange(6,2))

xs=fullrange(2,6)
ys=fullrange(6,2)
for i in range(len(xs)):
        print("x:", xs[i], "y:",ys[i])

with open(path) as file:
    lines = file.readlines()
    pprint(lines)

    vent_coords=[]
    print(vent_coords)
    for line in lines:
        line_coordinates =[]
        line = line.strip()
        print("Line: ",line)
        # split each line into start and end
        start_end = line.split(' -> ')
        print("start end: ", start_end)
        for i in range(len(start_end)):
            for j in start_end[i].split(','):
                line_coordinates.append(j)
        print("Line Coordinates", line_coordinates)
        vent_coords.append(line_coordinates)

np_vent_coordinates = np.array(vent_coords).astype(int)
print (np_vent_coordinates)
size = np.amax(np_vent_coordinates)+1

sea_floor_chart = np.zeros((size,size))
print (sea_floor_chart)

for vent in np_vent_coordinates:
    #filter non horizontal or vertical vents
    if vent[1] == vent[3] :
        print("horizontal: ", vent)
        x=vent[3]
        for y in fullrange(vent[0], vent[2]):
            sea_floor_chart[x][y]+=1
        print(sea_floor_chart)
        continue
    if vent[0] == vent[2]:
        print("Vertical: ", vent)
        y = vent[0]
        for x in fullrange(vent[1], vent[3]):
            sea_floor_chart[x][y]+=1
        print(sea_floor_chart)
        continue
    x=vent[1]
    y=vent[0]
    xs = fullrange(vent[1], vent[3])
    ys = fullrange(vent[0], vent[2])
    for i in range(len(xs)):
        print("x:", xs[i], "y:", ys[i])
        sea_floor_chart[xs[i]][ys[i]] += 1
        print(sea_floor_chart)

print(sea_floor_chart)

print (np.sum(sea_floor_chart>1))
exit(0)
# .......1..
# ..1....1..
# ..1....1..
# .......1..
# .112111211
# ..........
# ..........
# ..........
# ..........
# 222111....
#
# 1.1....11.
# .111...2..
# ..2.1.111.
# ...1.2.2..
# .112313211
# ...1.2....
# ..1...1...
# .1.....1..
# 1.......1.
# 222111....