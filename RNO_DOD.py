t = int(input())
count = 0
while count < t:
    n = int(input())
    m = input()
    A = m.split(' ')
    x = 0
    for i in A:
        x = x + int(i)
    print(x)
    count += 1
