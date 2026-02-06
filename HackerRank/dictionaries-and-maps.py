# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
phoneBook = {}
for _ in range(n):
    name, num = input().split()
    phoneBook[name] = num
while True:
    try:
        query = input().strip()
        if query in phoneBook:
            print(query + "=" + phoneBook[query])
        else:
            print("Not found")
    except:
        break
