def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    counter = 0
    while 0 in nums:
        counter += 1
        nums.remove(0)

    counter = [0 for _ in range(counter)]
    nums.extend(counter)
    return nums

nums = [0,1,0,3,12]
print(moveZeroes(nums))