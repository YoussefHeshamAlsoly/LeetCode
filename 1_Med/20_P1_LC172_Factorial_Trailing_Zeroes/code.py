# 172. Factorial Trailing Zeroes
# https://leetcode.com/problems/factorial-trailing-zeroes/description/

def trailingZeroes(n: int) -> int:
    # # My codeeeeee
    # for i in range(1, n+1):
    #     flag = i
    #     while flag%5==0:
    #         flag //= 5
    #         res += 1
    
    res = 0
    while n >= 5:
        n //= 5
        res += n
    return res

n = 30
print(trailingZeroes(n))