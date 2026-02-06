n = int(input())

for _ in range(n):
    a,b,c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    if a == b + c or b == a + c or c == a + b:
        print("YES")
    elif a != b + c or b != a + c or c != a + b:
        print("NO")