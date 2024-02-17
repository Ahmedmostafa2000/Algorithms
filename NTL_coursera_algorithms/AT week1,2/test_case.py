from random import randint
def test(n,maxnum):
    x = [0]*n
    for i in range(n):
        x[i] = randint(2,maxnum)
    return x