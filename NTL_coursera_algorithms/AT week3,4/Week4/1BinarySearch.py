def binary_search(box, key, start, end):
    if start>=end:
        return -1

    m = (start+end)//2
    if box[m]==key:
        return m
    if box[m]<=key:
        return binary_search(box, key, m+1, end)
    if box[m]>=key:
        return binary_search(box, key, start, m)


x = list(map(int, input().split()))
n = x[0]
box = x[1:len(x)]
x = list(map(int, input().split()))
k = x[0]
keys = x[1:len(x)]
x = 0

for i in range(k):
    print(binary_search(box, keys[i],0,n),end = ' ')





