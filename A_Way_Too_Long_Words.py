n = int(input())

for _ in range(n):
    word = input()
    lenWord = len(word)
    tooLong = ""
    if lenWord > 10:
        midValue = lenWord - 2
        tooLong = word[0] +  str(midValue) + word[-1]
        print(tooLong)
    else:
        print(word)
    