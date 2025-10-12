# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/description/

def productExceptSelf(nums: list[int]) -> list[int]:
    n = len(nums)
    answer = [1] * n

    left = 1
    for i in range(n):
        answer[i] = left
        left *= nums[i]

    right = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= right
        right *= nums[i]

    return answer





    # res = [0]*len(nums)
    # h = 1
    # for i in range(len(nums)):
    #     for j in range(len(nums)):
    #         if j == i:
    #             continue
    #         h *= nums[j]
    #     res[i] = h
    #     h = 1
    # return res

nums = [-1,1,0,-3,3]
x = productExceptSelf(nums)
print(x)
