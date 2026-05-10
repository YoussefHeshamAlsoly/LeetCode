# 162. Find Peak Element
# https://leetcode.com/problems/find-peak-element/description/


def findPeakElement(nums: list[int]):
    if len(nums) < 3:
        return (nums.index(max(nums)))
    
    Lptr = 0
    Cptr = 1
    Rptr = 2

    for _ in range (len(nums) - 2):
        if nums[Cptr] > nums[Rptr] and nums[Cptr] > nums[Lptr]:
            return Cptr
        Lptr += 1
        Cptr += 1
        Rptr += 1
    
    if nums[0] > nums[1]:
        return 0

    if nums[-1] > nums[-2]:
        return len(nums)-1


nums = [1,2,3,1]
print(findPeakElement(nums))