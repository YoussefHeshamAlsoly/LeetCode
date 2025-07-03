def findDisappearedNumbers(nums):
    s = set(nums)
    return [i for i in range(1, len(nums)+1) if i not in s]

nums = [1,1]
print(findDisappearedNumbers(nums))