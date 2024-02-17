n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
x.sort()
y.sort()
sum = 0
for i in range(n):
    sum += x[i]*y[i]
print(sum)