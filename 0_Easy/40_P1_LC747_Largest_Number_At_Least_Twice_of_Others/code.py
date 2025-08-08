def dominantIndex(nums:list):
    """
    :type nums: List[int]
    :rtype: int
    """
    for ind, value in enumerate(nums):
        if max(nums) >= 2*value:
            pass
        else:
            if nums.index(max(nums))==ind:
                continue
            return -1
    return nums.index(max(nums))

nums = [3,6,1,0]
print(dominantIndex(nums))
