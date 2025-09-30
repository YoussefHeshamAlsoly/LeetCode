# 201. Bitwise AND of Numbers Range
# https://leetcode.com/problems/bitwise-and-of-numbers-range/description/

def rangeBitwiseAnd(left: int, right: int) -> int:
    # DAAAAAAAAAAAAAAAAAAAAMN
    # res = []
    # current = 1
    # for i in range(left, right+1):
    #     current = current & i
        
    #     if current == 0 and '1' in res:
    #         print("here")
    #         res.extend(['0000000000000000']* ((right+1-i)//16) )
    #         res.extend(['0']* ((right+1-i)%16) )
    #         return int("".join(res), 2)

    #     res.append(str(current))
        
    #     print(f"i: {i}, current: {current}, res: {res}")
    
    # return int("".join(res), 2)

    # GOD I hate bit shit
    shift = 0
    while left < right:
        left >>= 1
        # if shift == 0 and left == 0:
        #     return 0
        right >>= 1
        shift += 1
    return left << shift

LR = [  1,
        2147483647
    ]

print("\nfinal res:", rangeBitwiseAnd(*LR))