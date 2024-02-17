from test_case import test,randint
def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product


def mine(x,n):
    if n != 2:
        big1 = x[0]
        big2 = x[0]
        for i in range(n):
            if big1 < x[i]:
                big1 = x[i]
        for i in range(n):
            if big2 < x[i] and x[i] != big1:
                big2 = x[i]
    return big1*big2

