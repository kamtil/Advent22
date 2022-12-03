import sys

priority = {
    1:"a", 2:"b", 3:"c", 4:"d", 5:"e", 6:"f", 7:"g",
    8:"h", 9:"i", 10:"j", 11:"k", 12:"l", 13:"m", 14:"n",
    15:"o", 16:"p", 17:"q", 18:"r", 19:"s", 20:"t", 21:"u",
    22:"v", 23:"w", 24:"x", 25:"y", 26:"z", 27:"A", 28:"B", 
    29:"C", 30:"D", 31:"E", 32:"F", 33:"G", 34:"H", 35:"I",
    36:"J", 37:"K", 38:"L", 39:"M", 40:"N", 41:"O", 42:"P",
    43:"Q", 44:"R", 45:"S", 46:"T", 47:"U", 48:"V", 49:"W",
    50:"X", 51:"Y", 52:"Z"          
}

def halveStrLen(strLine):
    l = int(len(strLine)/2)
    return l

def splitStr(strLine, leng, first):
    str2 = []
    if first:
        for i in range(leng):
            str2.append(strLine[i])
        return str2
    else:
        for i in range(leng):
            str2.append(strLine[i+leng])
        return str2

def compareStrings(str1, str2):
    for ch1 in str1:
        for ch2 in str2:
            if ch1 == ch2:  
                return ch1

def prioritize(ch):
    for k, v in priority.items():
        if v == ch:
            return k

def operate(strLine):
    w = halveStrLen(strLine)
    s1 = splitStr(strLine, w, True)
    s2 = splitStr(strLine, w, False)
    s3 = compareStrings(s1, s2)
    s4 = prioritize(s3)
    #diagnostics
    #print("full length", len(strLine), "halved length:", w, "matching letter:", s3, "priority:", s4)
    return s4

def compareTeamStrings(str1, str2, str3):
    for ch1 in str1:
        for ch2 in str2:
            for ch3 in str3:
                if ch3 == ch2:
                    if ch3 == ch1: 
                        return ch1

def countAllFileLines(fp):
    allLines = len(fp.readlines())
    f.seek(0)
    return allLines

enumerate(sys.argv)
try:
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
except:
    print("Usage: 3.py [--part1 | --part2] <filename>")
    exit(0)
whole = 0
if arg1 == "--part1" or arg1 == "-part1": 
    with open(arg2) as f:
    # PART 1 
        for line in f: 
            piece = operate(line)
            whole = whole + piece
        print("total:", whole)
elif arg1 == "--part2" or arg1 == "-part2": 
    with open(arg2) as f:
        # PART 2
        lineCount = countAllFileLines(f)
        for i in range(int(lineCount/3)):
            s1 = f.readline()
            s2 = f.readline()
            s3 = f.readline()
            piece = prioritize(compareTeamStrings(s1, s2, s3))
            whole = whole + piece
        print("total:", whole)    
else:
    print("Usage: 3.py [--part1 | --part2] <filename>")