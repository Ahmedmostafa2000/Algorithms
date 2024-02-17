
n = int(input())
if n == 0:
    print(0)
    exit()
if n == 1:
    print(1)
    exit()
if n == 2:
    print(2)
    exit()
a = 0
b = 1
x = []
for i in range(2,n+1):
    x = x + [a+b]
    a , b = b, b+a
print(sum(x)%10)