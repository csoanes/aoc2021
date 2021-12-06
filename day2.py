path = '/Users/root1/AoC2021Data/Day2/day2Data.txt'


with open(path) as file:
    depth=0
    locY=0
    attitude=0
    while line := file.readline().rstrip():
        print(line)
        instructionTuple = tuple(line.split());
        direction = instructionTuple[0];
        move = int(instructionTuple[1]);
        if direction =='forward':
            locY+=move
            depth+=move*attitude
        elif direction == 'up': attitude-=move
        elif direction == 'down': attitude+=move
        else: print("error unknown instruction");

        print ("Moved: ", direction, "by: ", move, "Location now: ", locY, " : ", depth, " Attidude: ", attitude)
    print ("Final Location: ", locY, ":", depth, " : ", locY*depth )
