def day06_part_one():

    # read in the line
    rfile = open("puzzle_input.txt", "r")
    line = list(rfile.readline().rstrip())

    for i in range(3, len(line)):

        curr_packet = line[i-3:i+1]

        if (len(curr_packet) == len(set(curr_packet))):
            return i+1

    return -1



def day06_part_two():

    # read in the line
    rfile = open("puzzle_input.txt", "r")
    line = list(rfile.readline().rstrip())

    for i in range(13, len(line)):

        curr_packet = line[i-13:i+1]

        if (len(curr_packet) == len(set(curr_packet))):
            return i+1

    return -1



if __name__=='__main__':
    print("Advent of Code: Day 06")
    print("Part One answer is " + str(day06_part_one()))
    print("Part Two answer is " + str(day06_part_two()))
