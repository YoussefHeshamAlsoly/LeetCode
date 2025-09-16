# 34. Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/


def searchRange(nums: list[int], target: int) -> list[int]:
    res = []
    
    try:
        res.append(nums.index(target))
    except Exception as e:
        return [-1, -1]
    
    nums = nums[::-1]
    res.append(len(nums) - nums.index(target) - 1)
    
    return res

nums = [5,7,7,8,8,10]
target = 8

print(searchRange(nums, target))