def sort_by_3st(x):
    for i in range(len(x)-1):
        for j in range(i+1,len(x)):
            if x[i][2]<x[j][2]:
                x[i], x[j] = x[j], x[i]
    return x


n, W = map(int, input().split())
x = [0]*n
V = 0
maxW = W
for i in range(n):
    x[i] = list(map(int, input().split()))
    x[i].append(x[i][0]/x[i][1])

x = sort_by_3st(x)

for i in range(n):
    if x[i][1] <= W and W > 0:
        W -= x[i][1]
        V += x[i][0]
        x[i][1] = 0
    else:
        if x[i][1] > 0 and W > 0:
            V += (W / x[i][1]) * x[i][0]
            W = 0



print("%.4f"%V)
