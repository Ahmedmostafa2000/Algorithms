def mine(x, n):
    big1 = 0
    big2 = 0
    index = 0
    for i in range(n):
        if big1 < x[i]:
            big1 = x[i]
            index = i
    for i in range(n):
        if big2 < x[i] and i != index:
            big2 = x[i]
    return big1*big2
n = int(input())
x = list(map(int,input().split()))
print(mine(x,n))