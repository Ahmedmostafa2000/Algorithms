n = int(input())
if n == 0:
    print(0)
    exit()
if n == 1:
    print(1)
    exit()

a = 0
b = 1
n -= 1
for i in range(n):
    a, b = b, a + b
print(b)