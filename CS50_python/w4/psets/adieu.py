import inflect

list = []
while True:
    try:
        name = input("Name: ").strip()
        list.append(name)
    except EOFError:
        print()
        break



p = inflect.engine()
text = p.join(list)

print(f"Adieu, adieu, to " + text)
