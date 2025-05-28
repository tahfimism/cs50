with open("students.csv") as file:
    for line in sorted(file):
        name, school = line.strip().split(",")
        print(f"{name} study in {school.strip()}")

