import csv

file = open("data.csv")
csvCursor = csv.DictReader(file)
for row in csvCursor:
    print(row["name"],row["score"],row["age"])
