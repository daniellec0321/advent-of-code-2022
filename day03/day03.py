def day03_part_one():

    ret = 0

    rfile = open("puzzle_input.txt", "r")
    curr = rfile.readline().rstrip()

    while curr:
        
        # split into substrings
        fsub = curr[0:int(len(curr)/2)]
        ssub = curr[int(len(curr)/2):int(len(curr))]

        # find common character
        for char in fsub:
            if char in ssub:

                # find priority level with ascii value
                ascii_value = ord(char)

                if ascii_value >= 97:
                    ret += (ascii_value - 96)
                else:
                    ret += (ascii_value - 38)

                break

        curr = rfile.readline().rstrip()

    return ret

def day03_part_two():

    ret = 0

    rfile = open("puzzle_input.txt", "r")
    curr0 = rfile.readline().rstrip()
    curr1 = rfile.readline().rstrip()
    curr2 = rfile.readline().rstrip()

    while curr0 and curr1 and curr2:

        # find their shared char
        for char in curr0:
            if (char in curr1) and (char in curr2):

                # find priority value
                ascii_value = ord(char)

                if ascii_value >= 97:
                    ret += (ascii_value - 96)
                else:
                    ret += (ascii_value - 38)

                break

        # read next lines
        curr0 = rfile.readline().rstrip()
        curr1 = rfile.readline().rstrip()
        curr2 = rfile.readline().rstrip()

    return ret



if __name__=='__main__':
    print("Advent of Code: Day 03")
    print("Part One answer is " + str(day03_part_one()))
    print("Part Two answer is " + str(day03_part_two()))
