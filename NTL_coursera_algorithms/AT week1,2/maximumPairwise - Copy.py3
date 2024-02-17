# from test_case import test
n = int(input())
# print(test(n,12))
# x = test(n,12)
x = list(map(int,input().split()))
if n==2:
    print(x[0]*x[1])
    exit()
big = x[0]
big2 = x[0]

for i in range(n):
    if big < x[i]:
        big2 = x[i]
    if big2 > big:
        big, big2 = big2, big
print(big*big2)
