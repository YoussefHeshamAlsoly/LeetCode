# 396. Rotate Function
# https://leetcode.com/problems/rotate-function/description/

def maxRotateFunction(nums: list[int]) -> int:
    def shift(array, key):
        return array[-key:] + array[:-key]
    
    n = 0
    res = 0
    max_res = 0
    
    while n < len(nums):
        for ind, element in enumerate(nums):
            res += ind*element
        
        max_res = max(max_res, res)
        # print(f"max_res: {max_res}, res: {res}, n:{n}")
        res = 0
        n += 1
        nums = shift(nums, key=1)
    
    return max_res

    # ChatGPT's code (thats the right solution by the way)
    # n = len(nums)
    # total = sum(nums)
    # f0 = sum(i * num for i, num in enumerate(nums))
    # best = f = f0

    # for k in range(1, n):
    #     f = f + total - n * nums[-k]
    #     best = max(best, f)

    # return best

nums = [18,4,13,-1,2,7,19,14,11,0,-9,9,4,2,-2,-7,18,18,-7,-5,9,6,-8,3,13,0,15,9,10,-1,17,13,13,-8,3,8,4,19,10,-8,18,15,11,13,11,1,14,2,10,1,11,5,18,5,-8,13,-10,5,-8,-9,-5,9,10,-10,-3,-3,-4,-4,-8,-10]
x = maxRotateFunction(nums)
print(x)