import numpy as np
from pprint import pprint

path = '/Users/root1/AoC2021Data/Day5/day5TestData.txt'


with open(path) as file:
    lines = file.readlines()
    pprint(lines)
    vent_coords = np.empty(shape=(0,len(lines)))
    print(vent_coords)
    for line in lines:
        line = line.strip()
        print("Line: ",line)
        # split each line into start and end
        start_end = line.split(' -> ')
        print("start end: ", start_end)
        start_end_strings = [tuple_string.split(',') for tuple_string in start_end]
        print ("Start end strings: ", start_end_strings)
        np_start_end_strings = np.array(start_end_strings)
        

print (vent_coords)