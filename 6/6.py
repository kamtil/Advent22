import sys

enumerate(sys.argv)
try:
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
except:
    print("Usage: 6.py [--part1 | --part2] <filename>")
    exit(0)

window = []

if arg1 == "--part1" or arg1 == "-part1": 
    with open(arg2) as f:
    # PART 1
        line = f.readline()
        for i in range(len(line)):
            if i < 4:
                window.append(line[i])
            else:
                if len(window) != len(set(window)): # if the length doesn't equal the sets, there is a duplicate
                    window.pop(0)                   # remove the first entry
                    window.append(line[i])          # append the next char in the list
                else:
                    print("Characters to process: ", i)
                    break
    print(window)

elif arg1 == "--part2" or arg1 == "-part2": 
    with open(arg2) as f:
    # PART 2
        line = f.readline()
        for i in range(len(line)):
            if i < 14:
                window.append(line[i])
            else:
                if len(window) != len(set(window)):
                    window.pop(0)
                    window.append(line[i])            
                else:
                    print("Characters to process: ", i)
                    break
    print(window)

else:
    print("Usage: 6.py [--part1 | --part2] <filename>")