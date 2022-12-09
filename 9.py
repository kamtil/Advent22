# track x,y axis first



def moveRight(steps):
    x = head[0]
    y = head[1]
    for i in range(steps):
        x += 1
        head[0] = x
        tailDiagonal()
        tailTrailRight()
        print("head:", head)
        print("tail:", tail)

def moveUp(steps):
    x = head[0]
    y = head[1]
    for i in range(steps):
        y += 1
        head[1] = y
        tailDiagonal()
        tailTrailRight()
        print("head:", head)
        print("tail:", tail)

def tailDiagonal():
    if tail[1] != head[1]: # if not on the same x axis
        if tail[1] > head[1]: # if the tail above the head
            if tail[0] < head[0]: # if the tail left to head
                print("tail above, to the left")
            else:
                print("tail above, to the right")
        elif tail[1] < head[1]: # if the tail below the head
            if tail[0] < head[0]: # if the tail left to head
                print("tail below, to the left")
                doesItTouch()
            else:
                print("tail below, to the right")
    else:
        print("on same row")

def tailTrailRight():
    if tail[0] + 2 == head[0]:
        print("tail following")
        tail[0] += 1
        addTrailHistory()

def doesItTouch():
    hX = head[0]
    hY = head[1]
    tX = tail[0]
    tY = tail[1]

    if hX >= tX + 1:
        if hY == tY + 1:
            print("touching diagonally on the left (above)")
        elif hY == tY - 1:
            print("touching diagonally on the left (below)")
        print("touching on the left")
        
    elif hX <= tX + 1:
        if hY == tY + 1:
            print("touching diagonally on the right (above)")
        elif hY == tY - 1:
            print("touching diagonally on the right (below)")
        print("touching on the right")

def addTrailHistory():
    strTail = str(tail[0]) + "x" + str(tail[1])
    tailHistory.append(strTail)

#put where the tail has been in a list, then run set on it to crush dupes len is answer


head = [0,0]
tail = [0,0]
tailHistory = []
start = [0,0]

addTrailHistory()
moveRight(4)
tailDiagonal()
tailTrailRight()
moveUp(4)
print(tailHistory)