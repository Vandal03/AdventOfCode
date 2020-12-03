validPass = 0
count = 0


passFile = open("passwords.txt")

for line in passFile:
    info = line.split()
    minMax = info[0].split("-")
    minLet = minMax[0]
    maxLet = minMax[1]
    letter = info[1][0]
   
    for c in info[2]:
        if c == letter:
            count += 1
    if count >= int(minLet) and count <= int(maxLet):
        validPass += 1
    count = 0

print(validPass)