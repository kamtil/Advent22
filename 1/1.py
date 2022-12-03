print("hello world")
list = {}
f = open("1.txt", "r")
calories = f.readlines()
elfNum = 1
w = 0
y = 0 
for line in calories: 
    if line != '\n':
        w = int(line) + w
    else: 
        list.update({elfNum: w})
        #print("Elf", elfNum, ": ", w)
        elfNum += 1
        w = 0
        
# list.sort()
# print(list[len(list)-1]) 
for e in sorted(list, key=list.get, reverse=False):
    print(e, ":", list[e])
    if e >= len(list) - 3:
        y = list[e] + y
#print(len(listS))
#for x in list:
#    print(list[x])
#    if x >= len(list) - 3:
#        y = list[x] + y
#print(x)
print(y)


#print(f.read())


# k = f.readline()
# if k != '\n':
#     k = int(k) + 2
#     print(k)
# f.close()
#print(y)
print("done")