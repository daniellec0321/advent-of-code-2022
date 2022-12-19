def day05_part_one():

    barge = dict()
    ret = ""

    rfile = open("puzzle_input.txt", "r")
    reading_barge = True

    curr = rfile.readline()

    while curr:

        # if reading the barge:
        if reading_barge:

            # if at the end of the barge: set flags and continue
            if curr[0] == ' ' and curr[1] == '1':

                reading_barge = False
                rfile.readline()
               
            # read in the barge
            else:

                # iterate through line
                for i in range(1, len(curr), 4):

                    # find what column we're in
                    col = int(i / 4) + 1
                    
                    # add crate to barge dictionary
                    if curr[i] != ' ':
                        
                        if col not in barge:
                            barge[col] = list()

                        barge[col].insert(0, curr[i])

        # read the move instruction
        else:

            # find num to move, where from, and where to
            curr = curr.rstrip().split(' ')
            num = int(curr[2])
            f = int(curr[4])
            t = int(curr[6])

            # loop, pop, and push from barge
            for i in range(0, num):

                if len(barge[f]) == 0:
                    break

                crate = barge[f].pop()
                barge[t].append(crate)

        curr = rfile.readline()

    # get ret string
    for i in range(1, len(barge)+1):
        ret += barge[i][-1]

    return ret



def day05_part_two():
    
    barge = dict()
    ret = ""

    rfile = open("puzzle_input.txt", "r")
    reading_barge = True

    curr = rfile.readline()

    while curr:

        # if reading the barge:
        if reading_barge:

            # if at the end of the barge: set flags and continue
            if curr[0] == ' ' and curr[1] == '1':

                reading_barge = False
                rfile.readline()
               
            # read in the barge
            else:

                # iterate through line
                for i in range(1, len(curr), 4):

                    # find what column we're in
                    col = int(i / 4) + 1
                    
                    # add crate to barge dictionary
                    if curr[i] != ' ':
                        
                        if col not in barge:
                            barge[col] = list()

                        barge[col].insert(0, curr[i])

        # read the move instruction
        else:

            # find num to move, where from, and where to
            curr = curr.rstrip().split(' ')
            num = int(curr[2])
            f = int(curr[4])
            t = int(curr[6])

            # create subarray and append
            crates = barge[f][len(barge[f])-num:len(barge[f])]
            barge[t].extend(crates)
            del barge[f][len(barge[f])-num:len(barge[f])]

        curr = rfile.readline()

    # get ret string
    for i in range(1, len(barge)+1):
        ret += barge[i][-1]

    return ret



def print_barge(barge):
    for col in barge:
        print("Col " + str(col) + ": ", end="")
        for crate in barge[col]:
            print(crate + ", ", end="")
        print("")



if __name__=='__main__':
    print("Advent of Code: Day 05")
    print("Part One answer is " + day05_part_one())
    print("Part Two answer is " + day05_part_two())
