x = 0
while x < 10:
    n = int(input())
    y = 0
    for i in range(1, n+1):
        y += i
    print(y)
    x += 1