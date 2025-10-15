# 137. Single Number II
# https://leetcode.com/problems/single-number-ii/description/

def singleNumber(nums: list[int]) -> int:
    seen = set()
    dublicates = set()

    for i in nums:
        if i in seen:
            dublicates.add(i)
        else:
            seen.add(i)
    
    return list(seen - dublicates)[0]

nums = [2,2,3,2]
x = singleNumber(nums)
print(x)
print(type(x))