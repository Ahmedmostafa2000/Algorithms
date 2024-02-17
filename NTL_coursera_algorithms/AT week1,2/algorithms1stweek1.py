def fibbonaci(n):
    root = (5**.5)
    return (1/root) * (((1+root) /2)**n - ((1-root)/2)**n)


for i in range(70,80):
    print(fibbonaci(i) , i,sep = '\t')
