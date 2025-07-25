import csv

with open("data.csv","r") as f:
    cc = csv.DictReader(f)
    for row in cc:
        print(row["name"],row["score"])
