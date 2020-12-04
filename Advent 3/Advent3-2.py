treeCount = 0
cPos = 0
runs = []
lineCount = 0
firstLine = True



def checkPos(x):
    global cPos
    cPos += x
    if cPos >= 31:
        cPos -= 31
        
def sled(x, y):
    f = open("hill.txt")
    global firstLine
    global cPos
    global lineCount
    global treeCount
    for line in f:
        if firstLine == True:
            firstLine = False
            lineCount +=1
            if line[cPos] == "#":
                treeCount += 1
                checkPos(x)
            else:
                checkPos(x) 
        elif lineCount == y:
            lineCount = 0
            lineCount += 1
            if line[cPos] == "#":
                treeCount += 1
                checkPos(x)
            else:
                checkPos(x)   
        else:
            lineCount += 1
    runs.append(treeCount)
    cPos = 0
    treeCount = 0
    lineCount = 0
    firstLine = True
    
            
sled(1,1)            
sled(3,1)
sled(5,1)
sled(7,1)
sled(1,2)

multi = runs[0] * runs[1] * runs[2] * runs[3] * runs[4]


print(multi)