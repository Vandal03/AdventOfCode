treeCount = 0
cPos = 0


f = open("hill.txt")


def checkPos():
    global cPos
    cPos += 3
    if cPos >= 31:
        cPos -= 31

for line in f:
    if line[cPos] == "#":
        treeCount += 1
        checkPos()
    else:
        checkPos()
            
print(treeCount)