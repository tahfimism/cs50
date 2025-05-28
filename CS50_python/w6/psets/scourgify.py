#test with name.csv

import sys
import csv

len = len(sys.argv)
if len < 3 :
    sys.exit("Too few command-line arguments")
elif len > 3:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].lower().endswith("csv"):
    sys.exit("input is not a csv file")
elif not sys.argv[2].lower().endswith("csv"):
    sys.exit("output is not a csv file")

list = []



try:
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            last, first = row[0].split(",")
            list.append([first.strip(), last.strip(), row[1]])
except FileNotFoundError:
    sys.exit("file not found")



try:
    with open(sys.argv[2], "w") as file:
        writer = csv.writer(file)
        writer.writerow(["first", "last", "house"])
        for row in list:
            writer.writerow(row)
except FileNotFoundError:
    sys.exit("file not found")
