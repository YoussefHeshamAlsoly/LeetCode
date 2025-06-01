def thirdMax(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = sorted(set(nums), reverse=True)
    if len(nums) >= 3:
        return nums[2]
    else:
        return max(nums)
    
    # return sorted(set(nums), reverse=True)[2] if len(set(nums))>=3 else max(sorted(set(nums), reverse=True))

print(thirdMax([1,1,2]))