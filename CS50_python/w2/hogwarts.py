
students = [
    {"name" : "nakib", "title" : "noor", "age" : "21"},
    {"name" : "luna", "title" : "good", "age" : "20"},
    {"name" : "nazeef", "title" : "khan", "age" : None},
]

for student in students:
    age = student["age"] if student["age"] is not None else "N/A"
    print(f"Name: {student["name"]:<10} Title: {student["title"]:<10} age: {student["age"]}")




