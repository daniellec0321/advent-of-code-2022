def day01_part_one():

    # set variables
    max_calories = 0
    curr_sum = 0

    # open file
    rfile = open("puzzle_input.txt", "r")

    curr = rfile.readline()

    # loop and read lines
    while curr:

        curr = curr.rstrip()
    
        # if at end of calorie sector
        if (curr == ''):
            
            # test current sum against max
            if (curr_sum > max_calories):
                max_calories = curr_sum

            # reset curr_sum
            curr_sum = 0

        # add to currsum
        else:
            curr_sum += int(curr)

        # read next line
        curr = rfile.readline()

    # test last sum
    if curr_sum > max_calories:
        max_calories = curr_sum

    return max_calories



def day01_part_two():

    # set variables, open, loop
    max_calories = [0] * 3
    curr_sum = 0

    rfile = open("puzzle_input.txt", "r")

    curr = rfile.readline()
    while curr:

        curr = curr.rstrip()

        # if at end of calorie sector
        if (curr == ''):

            # test current sum against the maxes
            if curr_sum > max_calories[0]:

                temp = max_calories[0]
                max_calories[0] = curr_sum

                temp1 = max_calories[1]
                max_calories[1] = temp

                max_calories[2] = temp1

            elif curr_sum > max_calories[1]:
                
                temp = max_calories[1]
                max_calories[1] = curr_sum

                max_calories[2] = temp

            elif curr_sum > max_calories[2]:

                max_calories[2] = curr_sum

            curr_sum = 0

        # add to sum
        else:
            curr_sum += int(curr)

        # read in new line
        curr = rfile.readline()

    # analyze last line
    if curr_sum > max_calories[0]:

        temp = max_calories[0]
        max_calories[0] = curr_sum

        temp1 = max_calories[1]
        max_calories[1] = temp

        max_calories[2] = temp1

    elif curr_sum > max_calories[1]:

        temp = max_calories[1]
        max_calories[1] = curr_sum

        max_calories[2] = temp

    elif curr_sum > max_calories[2]:

        max_calories[2] = curr_sum

    # sum the array values
    ret = max_calories[0] + max_calories[1] + max_calories[2]

    return ret



if __name__=='__main__':
    print("Advent of Code: Day 1")
    print("Part 1 answer is " + str(day01_part_one()))
    print("Part 2 answer is " + str(day01_part_two()))
