

due = 50
coins = [25, 10, 5]
while due > 0:
    print(f"Amount Due: {due}")
    coin = int(input("Insert Coin: "))

    if coin in coins:
        due = due - coin

print(f"Change Owed: {abs(due)}")


