def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    # original code
    # n = bin(n)[2:]
    # n = [int(i) for i in n]
    # return sum(n)

    # one liner
    return sum([int(i) for i in bin(n)[2:]])


print(hammingWeight(22))