
"""
with open("names.txt", "a") as file:
    file.write(f"{input("ur name? ")}\n")
"""

with open("names.txt", "r") as file:
    for line in sorted(file):
        print(line.strip())
