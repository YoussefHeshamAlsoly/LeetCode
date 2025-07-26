def differenceOfSums(n, m):
    """
    :type n: int
    :type m: int
    :rtype: int
    """
    # optimized to the best of MY CURRENT ability
    total_sum = ( n*(n+1) )/2
    for i in range(1, n+1):
        if i%m == 0:
            total_sum -= 2*i
    return int(total_sum)

    # total_sum = ( n*(n+1) )/2
    # div = 0

    # for i in list(range(1, n+1)):
    #     if i < m:
    #         pass
    #     else:
    #         if i%m == 0:
    #             div += i

    # return int(total_sum - (2 * div))

n = 10
m = 3

print(differenceOfSums(n, m))