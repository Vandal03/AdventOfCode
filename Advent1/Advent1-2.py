entriesFile = open("Entries.txt")
entries = []
desiredSum = 2020
total = 0


for line in entriesFile:
    entries.append(int(line))

i = 0
while i < len(entries):
    total += entries[i]
    j = i + 1
    while j  < len(entries):
        total = entries[i]
        total += entries[j]
        k = j + 1
        while k < len(entries):
            total += entries[k]
            if total == desiredSum:
                print(entries[i] * entries[j] * entries[k])
            else:
                total = total - entries[k]
            k += 1
        j += 1
    i += 1

print("Done")