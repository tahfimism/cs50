

import sys
from tabulate import tabulate
import csv

len = len(sys.argv)
if len < 2 :
    sys.exit("Too few command-line arguments")
elif len > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].lower().endswith("csv"):
    sys.exit("Not a csv file")

menu = []

with open(sys.argv[1]) as file:
    reader = csv.reader(file)
    for row in reader:
        menu.append([row[0], row[1], row[2]])





print(tabulate(menu, headers="firstrow", tablefmt="grid"))
