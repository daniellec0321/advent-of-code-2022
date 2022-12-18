def day02_part_one():

    score = 0

    # read through file
    rfile = open("puzzle_input.txt", "r")
    curr = rfile.readline().rstrip()

    while curr:

        # find if won or lost or draw
        if (curr[0] == 'A') and (curr[2] == 'X'):

            score += 4

        elif (curr[0] == 'A') and (curr[2] == 'Y'):

            score += 8

        elif (curr[0] == 'A') and (curr[2] == 'Z'):

            score += 3

        elif (curr[0] == 'B') and (curr[2] == 'X'):

            score += 1

        elif (curr[0] == 'B') and (curr[2] == 'Y'):

            score += 5

        elif (curr[0] == 'B') and (curr[2] == 'Z'):

            score += 9

        elif (curr[0] == 'C') and (curr[2] == 'X'):

            score += 7

        elif (curr[0] == 'C') and (curr[2] == 'Y'):

            score += 2

        else:

            score += 6

        curr = rfile.readline().rstrip()

    # return score
    return score



def day02_part_two():

    score = 0

    # read through file
    rfile = open("puzzle_input.txt", "r")
    curr = rfile.readline().rstrip()

    while curr:

        # find if won or lost or draw
        if (curr[0] == 'A') and (curr[2] == 'X'):

            score += 3

        elif (curr[0] == 'A') and (curr[2] == 'Y'):

            score += 4

        elif (curr[0] == 'A') and (curr[2] == 'Z'):

            score += 8

        elif (curr[0] == 'B') and (curr[2] == 'X'):

            score += 1

        elif (curr[0] == 'B') and (curr[2] == 'Y'):

            score += 5

        elif (curr[0] == 'B') and (curr[2] == 'Z'):

            score += 9

        elif (curr[0] == 'C') and (curr[2] == 'X'):

            score += 2

        elif (curr[0] == 'C') and (curr[2] == 'Y'):

            score += 6

        else:

            score += 7

        curr = rfile.readline().rstrip()

    # return score
    return score



if __name__=='__main__':
    print("Advent of Code: Day 02")
    print("The answer is " + str(day02_part_one()))
    print("The answer is " + str(day02_part_two()))
