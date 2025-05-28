
name = input("name? ")

match name.lower():
    case "nakib" | "noor":
        print("heyy")
    case "luna":
        print("yo")
    case _:
        print("no")
