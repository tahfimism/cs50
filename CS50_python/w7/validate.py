import re

mail = input("emani: ").strip()

if re.search(r"^[\w|\.]+@[\w|\.]+\.edu$", mail):
    print("valid")
else:
    print("invalid")

