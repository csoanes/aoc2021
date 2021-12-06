path = '/Users/root1/AoC2021Data/Day1/part1Input.txt'


with open(path) as file:
    prevdepth = 0;
    prevprevdepth=0
    sum=0;
    prevSum=0;
    deeperCount =0;
    while line := file.readline().rstrip():
        print("line:", line.rstrip())
        depth = int(line.rstrip())
        if prevprevdepth !=0:
            sum = depth + prevdepth + prevprevdepth;
            if prevSum != 0 and sum > prevSum:
                deeperCount+=1;
        print("sum: ",sum,"prevSum: ", prevSum, "deeperCount: ", deeperCount);


        prevprevdepth = prevdepth;
        prevdepth = depth;
        prevSum=sum;
    print ("final count: ",deeperCount)
