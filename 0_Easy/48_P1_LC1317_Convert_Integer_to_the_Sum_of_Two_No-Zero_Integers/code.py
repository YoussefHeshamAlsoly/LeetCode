def getNoZeroIntegers(n:int):
    """
    :type n: int
    :rtype: List[int]
    """

    mod = 10 ** (int (len(str(n)) / 2))
    n = [(n//mod)*mod, n%mod]
    flag = True
    while flag:
        if "0" in str(n[0]) or "0" in str(n[1]):
            n[0] -= 1
            n[1] += 1
        if "0" not in str(n[1]) and "0" not in str(n[0]):
            flag = False
    
    return n


n = 7
print(getNoZeroIntegers(n))