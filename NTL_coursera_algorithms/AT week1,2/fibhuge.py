n, m = map(int, input().split())
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
print(b,end = ' ')

if m == 0:
    print(0)
    exit()
if m == 1:
    print(1)
    exit()
a = 0
b = 1
n -= 1
for i in range(m):
    a, b = b, a + b
print(b)