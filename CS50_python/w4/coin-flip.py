import random
head = 0
tail = 0

lis = ["heads" , "tails"]
for i in range(100000):
    if random.choice(lis) == "heads":
        head += 1
    else:
        tail +=1

print(f"heads= {head}, tails= {tail}")

