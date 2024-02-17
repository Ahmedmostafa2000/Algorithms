from random import randint,choice


def testcases(n,maxnum):
    x = [0]*n
    for i in range(n):
        x[i] = randint(2,maxnum)
    return x


def part(start,arr,end):
    swapped = start+1
    for i in range(start+1, end):
        if arr[i] < arr[start]:
            arr[i], arr[swapped] = arr[swapped], arr[i]
            swapped += 1
    arr[start], arr[swapped-1] = arr[swapped-1], arr[start]
    return swapped-1


def quick_sort(start,arr,end):
    if start<end:
        swapped = part(start,arr,end)
        quick_sort(start, arr, swapped)
        quick_sort(swapped+1, arr, end)


def random_quick_sort(start,arr,end):
    if start<end:
        k = randint(start,end-1)
        arr[k],arr[start] = arr[start], arr[k]
        swapped = part(start,arr,end)
        quick_sort(start, arr, swapped)
        quick_sort(swapped+1, arr, end)



def test(x = testcases(12,30)):
    i=1
    y = sorted(x)
    while 1:
        random_quick_sort(0, x, len(x))
        if x==y:
            print("Passed test case number",i)
        else:
            print("Wrong answer on test case number",i)
            print(x)
            print(y)
            break
        i += 1
test()
#
# cong = list(map(int, input().split()))
# key = int(input())
