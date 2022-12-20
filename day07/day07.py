def day07_part_one():

    # STRING that holds our current path of directories (comma separated)
    path = ""
    path += "/"

    # dictionary that holds the files added for each directory
    files_found = dict()
    files_found["/"] = list()

    # dictionary that holds size of each directory
    sizes = dict()
    sizes["/"] = 0

    # read file
    rfile = open("puzzle_input.txt", "r")
    curr = rfile.readline().rstrip()

    while curr:

        curr = curr.split(' ')

        # if a command to cd
        if curr[0] == "$":

            # if changing directories
            if curr[1] == "cd":

                # pop from list
                if curr[2] == "..":

                    temp = path.split(",")
                    path = ""
                    temp.pop()
                    for i in range(0, len(temp)-1):
                        path += temp[i]
                        path += ","
                    path += temp[-1]

                # going to outermost directory
                elif curr[2] == "/":

                    path = "/"

                else:

                    path += ","
                    path += curr[2]

        # if reading out files/directories
        else:
            
            # reading out a file
            if curr[0] != "dir":

                # get each element on the path
                curr_dir = ""
                path_split = path.split(",")

                # iterate through each element in path
                for i in range(0, len(path_split)):

                    if i==0:
                        curr_dir += path_split[0]
                    else:
                        curr_dir += ","
                        curr_dir += path_split[i]

                    # if not in files found, add size
                    if (curr_dir not in files_found) or (curr[1] not in files_found[curr_dir]):

                        # add size
                        if curr_dir not in sizes:
                            sizes[curr_dir] = 0
                        sizes[curr_dir] += int(curr[0])

                        # add to files found
                        if curr_dir not in files_found:
                            files_found[curr_dir] = list()
                        files_found[curr_dir].append(curr[1])

        curr = rfile.readline().rstrip()

    # find sum of sizes
    ret = 0

    for elem in sizes:
        if sizes[elem] <= 100000:
            ret += sizes[elem]

    return ret



if __name__=='__main__':
    print("Advent of Code: Day 07")
    print("Part One answer is " + str(day07_part_one()))
