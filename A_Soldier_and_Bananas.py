k, n, w = map(int, input().split())

totalCost = 0
for num in range(1, w+1):
    totalCost += num * k
if totalCost <= n:
    print(0)
else:
    print(totalCost - n)