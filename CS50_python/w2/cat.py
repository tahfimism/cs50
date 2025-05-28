

def main():
    n = get_pos()
    meow(n)

def get_pos():
    while True:
        n = int(input("how many times? "))
        if n > 0:
            return n

def meow(n):
    print("meow\n" * n , end="")


main()



















'''
n = int(input("how many times? "))
for i in range(n):
    print("meow")

'''


'''
n = int(input("how many times? "))
i = 0
while i < n:
    print("meow")
    i += 1
'''
