# 179. Largest Number
# https://leetcode.com/problems/largest-number/description/

def largestNumber(nums: list[int]) -> str:
    nums = sorted(nums, key=lambda x:x / (10 ** len(str(x)) - 1 ), reverse=True)
    str_nums = [str(num) for num in nums]
    res = ''.join(str_nums)
    res = str(int(res))
    return res

nums = [3,30,34,5,9]
print(largestNumber(nums))
