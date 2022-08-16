import json
import csv

with open ("name_of_file.json", "r") as f:
    reader = csv.reader(f)
    #skip first line to avoid header being inserted
    next(reader)
    data = []
    for row in reader:
    data.append({"firstname":row[0],
    "age": row[1]
    })

with open ("name_of_file.csv", "w") as f:
    json.dump(data, f, indent=4)

#VERY GOOD VIDEO
#https://www.youtube.com/watch?v=LeFDBRAhRls