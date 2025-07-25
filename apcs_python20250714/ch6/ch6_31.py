fin = open("Poem.txt")
line = fin.readline()
while line:
    print(line,end="")
    line = fin.readline()
