n = int(input())
x = list(map(int,input().split()))
if n == 2:
    print(x[0]*x[1])
    exit()
big1 = x[0]
big2 = x[0]

for i in range(n):
    if big1 < x[i]:
        big1,big2 = x[i],big1
print(big1*big2)
