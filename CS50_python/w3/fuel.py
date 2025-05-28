
while True:
    try:
        nume , deno = input("Fraction: ").strip().split("/")
        if nume.isdigit() and deno.isdigit() and deno != "0":
            nume, deno = int(nume), int(deno)
            if deno >= nume:
                break
    except ValueError:
        pass

percent = (nume * 100)/deno
percent = round(percent)


if percent >= 99:
    print("F")
elif percent <= 1:
    print("E")
else:
    print(f"{round(percent)}%")

