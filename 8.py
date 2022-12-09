f = open("8.txt", "r") 

def getForestWidth(row):
    return len(row)

def getForestHeight(forest):
    return len(forest)

def viewForest():
    for row in forest:
        print(row)
    print(getForestWidth(forest), "x", getForestHeight(forest))

def buildForest():
    for line in f:
        x = line.strip()
        forest.append([*x])

def buildMap():
    x = 0
    y = 0
    for row in forest:
        x+=1
        for tree in row:
            if y >= width:
                y = 0
            y+=1
            key = str(x) + "x" + str(y)
            forestMap[key] = ["d"]

def setPerimiter():
    x = 0
    y = 0
    for row in forest: 
        x+=1
        for tree in row: 
            if y >= width:
                y = 0 
            y+=1           
            if x == 1 or x == height or y == 1 or y == width:
                key = str(x) + "x" + str(y)
                ignoreKeys.append(key)

def ignoreTrees():
    for key in ignoreKeys:
        if key in forestMap:
            forestMap[key] = ["_"]


def lookUp(sX, sY):
    tree = int(forest[sX][sY])
    print(sX)
    sX-=1
    while sX > -1:
        if tree > int(forest[sX][sY]):
            print("tree is visible")
        else:
            print("tree is not visible")
            return False
        sX-=1
    return True
def lookDown(sX, sY):
    tree = int(forest[sX][sY])
    print(sX)
    sX+=1
    while sX < height:
        if tree > int(forest[sX][sY]):
            print("tree is visible")
        else:
            print("tree is not visible")
            return False
        sX+=1
    return True
def lookLeft(sX, sY):
    tree = int(forest[sX][sY])
    print(sY)
    sY-=1
    while sY > -1:
        if tree > int(forest[sX][sY]):
            print("tree is visible")
        else:
            print("tree is not visible")
            return False
        sY-=1
    return True
def lookRight(sX, sY):
    tree = int(forest[sX][sY])
    print(sX)
    sY+=1
    while sY < width:
        if tree > int(forest[sX][sY]):
            print("tree is visible")
        else:
            print("tree is not visible")
            return False
        sY+=1
    return True

def scoreUp(sX, sY):
    tree = int(forest[sX][sY])
    sX-=1
    sco = 0
    while sX > -1:
        if tree > int(forest[sX][sY]):
            # print("tree is visible")
            sco +=1
        else:
            # print("tree is not visible")
            if sco == 0:
                return 1
            else:
                sco+=1
                return sco
        sX-=1
    return sco

def scoreDown(sX, sY):
    tree = int(forest[sX][sY])
    sX+=1
    sco = 0
    while sX < height:
        if tree > int(forest[sX][sY]):
            # print("tree is visible")
            sco +=1
        else:
            # print("tree is not visible")
            if sco == 0:
                return 1
            else:
                sco+=1
                return sco
        sX+=1
    return sco

def scoreLeft(sX, sY):
    tree = int(forest[sX][sY])
    # print(sY)
    sY-=1
    sco = 0
    while sY > -1:
        if tree > int(forest[sX][sY]):
            # print("tree is visible")
            sco += 1
        else:
            # print("tree is not visible")
            if sco == 0:
                return 1
            else:
                sco+=1
                return sco
        sY-=1
    return sco

def scoreRight(sX, sY):
    tree = int(forest[sX][sY])
    # print(sY)
    sY+=1
    sco = 0
    while sY < width:
        if tree > int(forest[sX][sY]):
            # print("tree is visible")
            sco += 1
        else:
            # print("tree is not visible")
            if sco == 0:
                return 1
            else:
                sco+=1
                return sco
        sY+=1
    return sco


def perform():
    for key in forestMap:
        if forestMap[key] != ["_"]:
            sK = key.split("x")
            print(sK)
            sX = int(sK[0])-1
            sY = int(sK[1])-1

            if lookUp(sX,sY):
                forestMap[key].append("u")
            if lookDown(sX,sY):
                forestMap[key].append("w")
            if lookLeft(sX,sY):
                forestMap[key].append("l")
            if lookRight(sX,sY):
                forestMap[key].append("r")
            if forestMap[key] == ["d"]:
                forestMap[key].pop()

def score():
    biggestSceneScore = 0
    scenic = 0
    for key in forestMap:
        if forestMap[key] != ["_"]:
            sK = key.split("x")
            # print(key)
            sX = int(sK[0])-1
            sY = int(sK[1])-1

            scU = scoreUp(sX,sY)
            scD = scoreDown(sX,sY)
            scL = scoreLeft(sX,sY)
            scR = scoreRight(sX,sY)

            # print("scoreUp:", scU)
            # print("scoreDw:", scD)
            # print("scoreLf:", scL)
            # print("scoreRi:", scR)

            scenic = scU * scD * scL * scR
            print(key, "scenic score: ", scenic)
            if scenic >= biggestSceneScore:
                sceneKey = key
                biggestSceneScore = scenic
    print("Best scene:", sceneKey, "Score: ", biggestSceneScore)

def visibleTrees():
    count = 0
    for key in forestMap:
        if '_' in forestMap[key] or 'd' in forestMap[key]:
            count += 1
    print("visible trees from perimeter: ", count)

forest = []
forestMap = {}
ignoreKeys = []


buildForest()


width = getForestWidth(forest[0])
height = getForestHeight(forest)

buildMap()

viewForest()

#print(forestMap)
setPerimiter()
ignoreTrees()
score()
#print(forestMap)
visibleTrees()
