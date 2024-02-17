from test_case import test
from test_case import randint
def mine(x,n):
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
    print(big1,big2)
    return big1*big2
# n = int(input())
# x = list(map(int,input().split()))
count = 1
while 1:

    n = randint(3, 1000)
    x = test(n, 50)
    max = x[0]*x[1]
    for i in range(n-1):
        for j in range(i+1, n):
            if x[i]*x[j] > max:
                max = x[i]*x[j]
    other = mine(x,n)
    if max != other:
        # print("wrong answer on test number",count,sorted(x,reverse= 1)[0],sorted(x,reverse= 1)[1],max,other,sep = "\t\t")
        # print(sorted(x,reverse= 1))
        # print(x)
        break
    count += 1
    print(count)
