def gcd(m,n):
    if n == 0:
        return m
    remain = m % n
    return gcd(n, remain)

def lcm(m,n):
    return (m*n)/gcd(m,n)


m, n = map(int, input().split())
print(int(lcm(m,n)))