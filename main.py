def bear(berries, n):
    while berries[0:n:2] > berries[1:n:2]:
        return str(berries[0:n:2])
    else:
        return str(berries[1:n:2])


file = open("input.txt", "r")
fileout = open('output.txt', 'w')
forestLen = len(file.readlines())
with open("input.txt") as f:
    forest = f.readlines()
    for i in range(forestLen):
        level = forest[i].split()
        level = list(map(int, level))
        levelLen = len(level)
        a = bear(level, levelLen)
        fileout.writelines(a + "\n")
fileout.close()
file.close()
