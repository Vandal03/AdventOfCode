validPass = 0
count = 0


passFile = open("passwords.txt")

for line in passFile:
    info = line.split()
    pos = info[0].split("-")
    pos1 = pos[0]
    pos2 = pos[1]
    letter = info[1][0]
   
    if letter == info[2][int(pos1)-1] and letter != info[2][int(pos2)-1]:
        validPass += 1
    elif letter != info[2][int(pos1)-1] and letter == info[2][int(pos2)-1]:
        validPass +=1

print(validPass)