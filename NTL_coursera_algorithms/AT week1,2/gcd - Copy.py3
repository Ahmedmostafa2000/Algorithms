def gcd(m,n):
    if n == 0:
        return m
    remain = m % n
    return gcd(n, remain)


m, n = map(int, input().split())
print(gcd(m,n))