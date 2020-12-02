entriesFile = open("Entries.txt")
entries = []
desiredSum = 2020
search = 0

for line in entriesFile:
    entries.append(int(line))

i = 0
while i < len(entries):
    search = desiredSum - entries[i]
    exists = search in entries
    if exists == True:
       print(str(entries[i]) + " " + str(search) + " = " + str((entries[i] * search)))
       break
    i += 1

print("Done")