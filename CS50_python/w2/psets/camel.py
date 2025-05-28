


text= input("camelCase: ").strip()
print("snake_case: ", end="")
for c in text:
    if c.isupper():
        print(f"_{c.lower()}", end="")
    else:
        print(c, end="")
print()



