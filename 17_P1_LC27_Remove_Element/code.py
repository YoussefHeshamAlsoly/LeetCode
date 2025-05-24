def removeElement(nums:list, val:int):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    i = 0
    while i < len(nums):
        try:
            if nums[i] == val:
                nums.pop(i)
                i -= 1
        except IndexError:
            pass
        i += 1
    return (nums)

nums = [3,2,2,3]
value = 3

print(removeElement(nums, value))