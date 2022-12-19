def day04_part_one():

    ret = 0
    rfile = open("puzzle_input.txt", "r")
    curr = rfile.readline().rstrip()

    while curr:

        e1zone1 = int((curr.split(',')[0]).split('-')[0])
        e1zone2 = int((curr.split(',')[0]).split('-')[1])
        e2zone1 = int((curr.split(',')[1]).split('-')[0])
        e2zone2 = int((curr.split(',')[1]).split('-')[1])

        # e1 fully contains e2
        if e1zone1 <= e2zone1 and e1zone2 >= e2zone2:
            ret += 1
        elif e2zone1 <= e1zone1 and e2zone2 >= e1zone2:
            ret += 1

        curr = rfile.readline().rstrip()

    return ret



if __name__=='__main__':
    print("Advent of Code: Day 04")
    print("Part One answer is " + str(day04_part_one()))
