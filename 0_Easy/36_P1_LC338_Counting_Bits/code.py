def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    return [(bin(i)).count("1") for i in range(n+1)]


x = 5
print(countBits(x))