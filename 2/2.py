battle = ["", ""]
final = 0

def checkTheirHand(choice):
    ind = 0 
    #print("hello")
    for entry in h1:
        if choice == entry:
            indexCheck(True, ind)
        else:
            ind += 1

def checkMyHand(choice):
    ind = 0
    #print("goodbye")
    for entry in h2:
        if choice == entry:
            indexCheck(False, ind)
        else:
            ind += 1

def indexCheck(their, ind):
    if their:
        if ind == 0:
            battle[0] = "rock"
        elif ind == 1:
            battle[0] = "paper"
        elif ind == 2: 
            battle[0] = "scissors"
    else:
        if ind == 0:
            battle[1] = "rock"
        elif ind == 1:
            battle[1] = "paper"
        elif ind == 2: 
            battle[1] = "scissors"

def resetBattle():
    for i in range(len(battle)):
        battle[i] = ""

def score(theirHand, myHand):
    if theirHand == "rock":
        if myHand == "rock":
            s1 = 1
            s = s1 + 3
        elif myHand == "paper":
            s1 = 2
            s = s1 + 6
        elif myHand == "scissors":
            s1 = 3
            s = s1 + 0
    elif theirHand == "paper":
        if myHand == "rock":
            s1 = 1
            s = s1 + 0
        elif myHand == "paper":
            s1 = 2
            s = s1 + 3
        elif myHand == "scissors":
            s1 = 3
            s = s1 + 6
    elif theirHand == "scissors":
        if myHand == "rock":
            s1 = 1
            s = s1 + 6
        elif myHand == "paper":
            s1 = 2
            s = s1 + 0
        elif myHand == "scissors":
            s1 = 3
            s = s1 + 3
    return s

def fight():
    sc = score(battle[0], battle[1])
    print(battle[0], "vs", battle[1], "----", sc)
    #print(s)    
    return sc

def cheat(theirHand, condition):
    if theirHand == "rock":
        if condition == "X": # lose
            battle[1] = "scissors"
        elif condition == "Y": # draw
            battle[1] = "rock"
        elif condition == "Z": # win
            battle[1] = "paper"
    elif theirHand == "paper": 
        if condition == "X": # lose
            battle[1] = "rock"
        if condition == "Y": # draw
            battle[1] = "paper"
        if condition == "Z": # win
            battle[1] = "scissors" 
    elif theirHand == "scissors": 
        if condition == "X": # lose
            battle[1] = "paper"
        if condition == "Y": # draw
            battle[1] = "scissors"
        if condition == "Z": # win
            battle[1] = "rock" 

h1 = ["A", "B", "C"]
h2 = ["X", "Y", "Z"]

print("hello world")

f = open("2.txt", "r")

# DON'T CHEAT
#print(w[0], w[2])
# for line in f: 
#     checkTheirHand(line[0])
#     checkMyHand(line[2])
#     s = fight()
#     final = final + s
#     resetBattle()

# CHEAT
for line in f:
    checkTheirHand(line[0])
    cheat(battle[0], line[2])
    s = fight()
    final = final + s
    resetBattle()

f.close()

print("Final score:", final)