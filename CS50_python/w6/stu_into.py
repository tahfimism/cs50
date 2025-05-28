import csv

name = input("name: ")
school = input("school: ")


with open("stu_info.csv") as file:
    writter = csv.DictWriter(file, fieldnames=["name", "school"])
    writter.writerow({"name" : name, "school" : school})
 