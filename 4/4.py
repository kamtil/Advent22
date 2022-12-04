import sys

# splits the lines in to individual ranges. for instance: 1-2,3-4 -->> ["1", "-", "2"] ["3", "-", "4"] 
def splitRange(line, first):
    numList = []
    if first:
        for c in line:
            if c.isdigit() or c == '-':
                numList.append(c)
            elif c == ',':
                break
        return numList
    else:
        splitNow = False
        for c in line:
            if c == ',':
                splitNow = True
            if splitNow:
                if c.isdigit() or c == '-':
                    numList.append(c)
        return numList

# converts strings (representing integers) in the list to integers ex: ["1", "-", "2"] -->> 1 & 2
def createInts(list):
    before = True
    cv = ""
    cx = ""
    for c in list:
        if c.isdigit() and before:
            cv = cv + c
        elif c.isdigit() and (not before):
            cx = cx + c
        elif c == '-':
            before = False
    return int(cv), int(cx)

# create list containing conents of range setRange(5,8) -->> [5, 6, 7, 8]
def setRange(i1, i2): 
    numList = []
    if i1 <= i2:
        for w in range(i1, i2+1):
            numList.append(w)
        #print(numList)
        return numList
    else:
        print("invalid range")

# checks if lists are enveloped by each other
def isEnveloped(list1, list2):
    enveloped = True
    for i in list1:
        if (i in list2):
            continue
        else:
            enveloped = False
    # if enveloped:
    #    print(list1, "is enveloped by\n", list2)
    #else:
    if not enveloped:
        enveloped = True
        for i in list2:
            if (i in list1):
                continue
            else:
                enveloped = False
        # if enveloped:
        #     print(list2, "is enveloped by\n", list1)
    return enveloped

# checks if any value in a list is an element of another list (overlap)
def anyOverlap(list1,list2):
    overlap = False
    for i in list1:
        if (i in list2):
            overlap = True
    # if overlap:
    #     print(list1, "overlaps with", list2)
    if not overlap:
        for i in list2:
            if (i in list1):
                overlap = True
    # if overlap:
    #     print(list2, "overlaps with", list1)
    return overlap

enumerate(sys.argv)
try:
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
except:
    print("Usage: 4.py [--part1 | --part2] <filename>")
    exit(0)

final = 0
if arg1 == "--part1" or arg1 == "-part1": 
    with open(arg2) as f:
    # PART 1
        for line in f:
            e = splitRange(line, True)
            g = splitRange(line, False)
            #print(g)
            h, i = createInts(e)
            #print(h, i)
            hR = setRange(h,i)
            #print(hR)
            j, k = createInts(g)
            jR = setRange(j,k)
            #print(jR)
            s = isEnveloped(hR, jR)
            #print(j, k)
            if s:
                final +=1
            #print(line)
        print("Enveloped ranges:", final)
elif arg1 == "--part2" or arg1 == "-part2": 
    with open(arg2) as f:
        for line in f:
            e = splitRange(line, True)
            #print(e)
            g = splitRange(line, False)
            #print(g)
            h, i = createInts(e)
            #print(h, i)
            hR = setRange(h,i)
            #print(hR)
            j, k = createInts(g)
            jR = setRange(j,k)
            #print(jR)
            s = anyOverlap(hR,jR)
            #print(j, k)
            if s:
                final +=1
            #print(line)
        print("Overlapping ranges:", final)
else: 
    print("Usage: 4.py [--part1 | --part2] <filename>")