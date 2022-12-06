import sys

# determine number of rows / how tall the stack of boxes is 
def getMap(fp):
    height = 0
    widthArr = []
    for line in fp:
        if '[' in line:
            print(line)
            height += 1
        elif line[1].isdigit():
            print(line)
            for c in line:
                if c.isdigit():
                    widthArr.append(c)   
            break
    return height, int(max(widthArr))

# parse the content of each row. letters denote crates, '-' is an empty space 
def viewCrates(line):
    count = 0
    rowOfCrates = []
    spaceCount = 0
    for c in line:
        if c.isspace():
            spaceCount += 1
        if spaceCount == 4:
            rowOfCrates.append("-")
            spaceCount = 0
        if c.isalpha():
            rowOfCrates.append(c)
            spaceCount = 0
    return rowOfCrates

# turn txt file into something i can interact with 
def createInteractiveCrateMap(fx, two_D_Array, height):
    fx.seek(0)
    for i in range(height):
        line = fx.readline()
        #print(line)
        two_D_Array.append(viewCrates(line))
    fx.readline()
    fx.readline()
    return two_D_Array

# column number matches the one on file, not in the array!
def howHigh(intCrateMap, column):
    thisHigh = 0
    for i in range(len(intCrateMap)):
        #print(intCrateMap[i][column-1])
        if intCrateMap[i][column-1].isalpha():
            thisHigh +=1
    return thisHigh

# parse each instruction (extract each argument)
def parseCommand(line):
    banana = line.split(" ")
    mov = banana[1]
    src = banana[3]
    dst = banana[5]
    return int(mov), int(src), int(dst)

# make a new row (increase height)
def createRow(intCrateMap):
    intCrateMap.append([])
    for i in range(maxWidth):
        intCrateMap[len(intCrateMap)-1].append("-")

# move crates around, replacing them with "-" as they are moved from their source
# cratemover 9000 mode -- move one crate at a time, order reversed
def moveCrates(intCrateMap, mov, src, dst):
    for i in range(mov):
        height = howHigh(intCrateMap, src)
        #print(height)
        #print(intCrateMap[height-1][src-1])
        srcCrate = intCrateMap[height-1][src-1]
        intCrateMap[height-1][src-1] = "-"

        height = howHigh(intCrateMap, dst)
        #print(intCrateMap[height-1][dst-1])
        if height >= len(intCrateMap):
            createRow(intCrateMap)
            intCrateMap[height][dst-1] = srcCrate
        else:
            intCrateMap[height][dst-1] = srcCrate

# cratemover 9001 mode -- move stacks of crates and preserve their ordrer
def moveStack(intCrateMap, mov, src, dst):
    srcStack = []
    height = howHigh(intCrateMap, src)
    #print(height)
    for i in range(mov):
        srcStack.append(intCrateMap[height-i-1][src-1])
        intCrateMap[height-i-1][src-1] = "-"

    height = howHigh(intCrateMap, dst)
    #print(srcStack)
    if height+len(srcStack) >= len(intCrateMap):
        diff = (height+len(srcStack))-len(intCrateMap)
        for i in range(diff):
            createRow(intCrateMap)
        j = len(srcStack)
        for i in range(mov):
            intCrateMap[height+i][dst-1] = srcStack[j-1]
            j -= 1
    else:
        j = len(srcStack)
        for i in range(mov):
            intCrateMap[height+i][dst-1] = srcStack[j-1]
            j -= 1

# display the pile of crates at any time
def showCurrentPile():
    print("-----------------------------")
    for i in range(len(intCrateMap)-1, -1, -1):
        print(intCrateMap[i])
    print("-----------------------------")

enumerate(sys.argv)
try:
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
except:
    print("Usage: 5.py [--part1 | --part2] <filename>")
    exit(0)

if arg1 == "--part1" or arg1 == "-part1": 
    with open(arg2) as f:
    # PART 1
        maxHeight, maxWidth = getMap(f)
        intCrateMap = []
        intCrateMap = createInteractiveCrateMap(f, intCrateMap, maxHeight)
        intCrateMap.reverse() # reverse order for easier understanding
        for line in f:
            #print(line)
            m, s, d = parseCommand(line)
            moveCrates(intCrateMap, m, s, d)
        showCurrentPile()

elif arg1 == "--part2" or arg1 == "-part2": 
    with open(arg2) as f:
    # PART 2
        maxHeight, maxWidth = getMap(f)
        intCrateMap = []
        intCrateMap = createInteractiveCrateMap(f, intCrateMap, maxHeight)
        intCrateMap.reverse() # reverse order for easier understanding
        for line in f:
            #print(line)
            m, s, d = parseCommand(line)
            moveStack(intCrateMap, m, s, d)
        showCurrentPile()
else: 
    print("Usage: 5.py [--part1 | --part2] <filename>")