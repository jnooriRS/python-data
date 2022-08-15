import csv
import json

with open ("name_of_file.json", "r") as f:
    data = json.load(f)
    names = data["names"]

with open ("name)of_file.csv", "w") as f:
    fieldnames = names[0].keys()
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writerheader()
    for name in names:
        writer.writerow(name)
#https://www.youtube.com/watch?v=YLCSVv46ERo