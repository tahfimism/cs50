
list = []
while True:
    try:
        list.append(input().strip().upper())
    except EOFError:

        break

list.sort()
sets = sorted(set(list))
for item in sets:
    print(f"{list.count(item)} {item}")


