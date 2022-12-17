def day01():

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

if __name__=='__main__':
    print("Advent of Code: Day 1")
    print("Answer is " + str(day01()))
