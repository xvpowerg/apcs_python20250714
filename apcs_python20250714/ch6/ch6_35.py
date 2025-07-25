import csv
file = open("data2.csv")
csvCusor = csv.reader(file)

for row in csvCusor:
    print(row[0],row[2])
file.close()    
