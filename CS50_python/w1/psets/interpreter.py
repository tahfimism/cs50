
text = input("Expression: ").split(" ")

first = float(text[0])
second = float(text[2])
opp = text[1]

match opp:
    case "+":
        print(first + second)
    case "-":
        print(first - second)
    case "*":
        print(first * second)
    case "/":
        print(first / second)


