

def isCommand():
    if st[0] == "$":
        return True
    return False

def parseCommand():
    global wd
    if st[1] == "cd":
        wd = st[2]
        if wd == "..":
            wdHistory.pop()
        else:
            wdHistory.append(wd)
            print("changing dir to", st[2])
            if st[2] == root["name"]:
                print("you are in root!")
    elif st[1] == "ls":
        print("listing directory contents of ", wd)

    else:
        print("i am broken")

def parseOutput():
    if st[0] == "dir":
        temp = {
            "parent": wd,
            "name": st[1],
            "files": [],
            "childDirs": [],
            "size": 0,
            "isDir": True
        }
        
        keyName = "dir_" + temp["name"]
        print("KEY NAME: ", keyName)
        filesystem[keyName] = temp
        if wd == "/":
            print("history is:", wdHistory)
            if wd not in filesystem["root"]["childDirs"]:
                filesystem["root"]["childDirs"].append(st[1])
        else:
            print("not in root, history is:", wdHistory)
            # get the name of one folder up
            if wdHistory[len(wdHistory)-1] == "/":
                keyName = "root"
            else:
                keyName = "dir_" + wd
            print("AT FOLDER:", st[1], "PREVIOUS FOLDER", wdHistory[len(wdHistory)-1], "CHILD KEY NAME: ", keyName)
            if wd not in filesystem[keyName]["childDirs"]:
                filesystem[keyName]["childDirs"].append(st[1])
    elif st[0].isdigit():
        print("this is a file.")
        if wd != "/":
            temp = {st[1]:st[0]}
            keyName = "dir_" + wd
            filesystem[keyName]["files"].append(temp)
        else:
            temp = {st[1]:st[0]}
            filesystem["root"]["files"].append(temp)

def calcDirSize():
    for directories in filesystem:
        dirs.append(filesystem[directories]["name"])
    # print(filesystem[entries]["files"], "\n")
        partialSize = 0
        for files in filesystem[directories]["files"]:
            fileSize = int(list(files.values())[0]) # gotta love type conversions
            #print(fileSize)
            partialSize = partialSize + fileSize
        filesystem[directories]["size"] = partialSize
        

def getAllDirSizes(cap):
    totalSize = 0
    for directories in filesystem:
        dirSize = filesystem[directories]["size"]
        if dirSize <= cap:
            totalSize = totalSize + dirSize
    print("it's always the same number ", totalSize)

def getDirSize(directory):
    global filesystem
    if directory == "/":
        keyName = "root"
    else:
        keyName = "dir_" + directory
    return filesystem[keyName]["size"]

def countTheChildren():
    cappedTotal = 0
    for directories in filesystem:
        if directories != "root":
            dirSize = filesystem[directories]["size"]
            print("found parent: ", filesystem[directories]["name"], "size: ", dirSize)
            if filesystem[directories]["childDirs"] != []:
                for child in filesystem[directories]["childDirs"]:
                    cSize = getDirSize(child)
                    print("found child ", child, "size: ", cSize)
                    print("before ", filesystem[directories]["size"])
                    filesystem[directories]["size"] += cSize
                    print("after ", filesystem[directories]["size"])
                    
                    # if cSize <= cap:
                    #     cappedTotal = cappedTotal + cSize
            
            #if dirSize <= cap:
                #cappedTotal = cappedTotal + dirSize                    
                    #print("CHILDREN: ", filesystem[directories]["childDirs"]) 
        #print(cappedTotal) 

def countTheChildren2():
    for directories in filesystem:
        if directories != "root":
            dirSize = filesystem[directories]["size"]
            if filesystem[directories]["parent"] != "/":
                parent = filesystem[directories]["parent"]
                keyName = "dir_" + parent
                filesystem[keyName]["size"] += dirSize

def countTheChildren3():
    for folder in dirs:
        if folder != "/":
            keyName = "dir_" + folder
            dirSize = filesystem[keyName]["size"]
            print("found parent: ", filesystem[keyName]["name"], "size: ", dirSize)
            if filesystem[keyName]["childDirs"] != []:
                for child in filesystem[keyName]["childDirs"]:
                    cSize = getDirSize(child)
                    print("found child ", child, "size: ", cSize)
                    print("before ", filesystem[keyName]["size"])
                    filesystem[keyName]["size"] += cSize
                    print("after ", filesystem[keyName]["size"])


def rootSize():
    for directories in filesystem:
        if directories == "root":
            dirSize = filesystem[directories]["size"]
            for child in filesystem[directories]["childDirs"]:
                    cSize = getDirSize(child)
                    print("found child ", child, "size: ", cSize)
                    print("before ", filesystem[directories]["size"])
                    filesystem[directories]["size"] += cSize
                    print("after ", filesystem[directories]["size"])


wd = ""
wdHistory = []
dirs = []

root = {
    "parent": "me",
    "name": "/",
    "files": [],
    "childDirs": [],
    "size": 0,
    "isDir": True
}

filesystem = {
    "root": root
}

print("hello world")
file = open("7.txt", "r")
for line in file:
    st = line.strip("\n") # remove \n
    st = st.split()
    if isCommand():
        parseCommand()
    else:
        print(line, "is command output")
        parseOutput()



totalSize = 0
partialSize = 0
# for entries in filesystem:
#     # print(filesystem[entries]["files"], "\n")
#     for files in filesystem[entries]["files"]:
#         fileSize = int(list(files.values())[0]) # gotta love type conversions
#         #print(fileSize)
#         partialSize = partialSize + fileSize
#     if partialSize <= 100000:
#         print("this size can be added", partialSize)
#         totalSize = totalSize + partialSize
#         partialSize = 0
#     else:
#         partialSize = 0
# print(totalSize)

x=0
calcDirSize()
print("SIZE BEFORE -----------------------------------")
for dir in filesystem:
    print(filesystem[dir]["name"], "size ", filesystem[dir]["size"])
print("-----------------------------------")
countTheChildren3()
rootSize()
print("SIZE AFTER -----------------------------------")
for dir in filesystem:
    print(filesystem[dir]["name"], "size ", filesystem[dir]["size"])
    if filesystem[dir]["size"] <= 100000:
        x += filesystem[dir]["size"]
print("-----------------------------------")
getAllDirSizes(100000)




for dir in filesystem:
#    print(filesystem[dir].values())
    if filesystem[dir]["size"] == 0:
        if filesystem[dir]["childDirs"] != []:
                for child in filesystem[dir]["childDirs"]:
                    cSize = getDirSize(child)
                    print("found child ", child, "size: ", cSize)
                    print("before ", filesystem[dir]["size"])
                    filesystem[dir]["size"] += cSize
                    print("after ", filesystem[dir]["size"])

rootSize()

dirs.reverse()
print(dirs)


getAllDirSizes(100000)



file.close()