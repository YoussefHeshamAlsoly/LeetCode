import math
def isPowerOfFour(n):
    """
    :type n: int
    :rtype: List[int]
    """
    if n <= 0:
        return False
    # i dont remember the log identities so that's that. just an approximation.
    res = int((math.log(n*math.e) + math.log10(n)) / 2)
    if n == 4**res or n == 4**(res+1) or n == 4**(res-1):
        return True
    else:
        return False

x = 0

print(isPowerOfFour(x))