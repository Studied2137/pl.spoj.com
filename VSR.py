t = int(input())
count = 0
B = []
while count < t:
    V = []
    v = input()
    V.extend(v.split(' '))
    B.append(int((2*(int(V[0])*int(V[1])))/(int(V[0])+int(V[1]))))
    count += 1
for i in B:
    print(i)
