# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
phoneBook = {}
for _ in range(n):
    name, num = input().split()
    phoneBook[name] = num
for _ in range(n):
    name = input()
    if name in phoneBook:
        print(f"{name}={phoneBook[name]}")
    else:
        print("Not found")
