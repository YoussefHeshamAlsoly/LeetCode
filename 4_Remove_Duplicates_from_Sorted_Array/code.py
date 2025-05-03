
# # The following is a script that actually works

# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums:
#             return 0
#         insert_position = 1
#         for unique in range(1, len(nums)):
#             if nums[unique] != nums[unique-1]:
#                 nums[insert_position] = nums[unique]
#                 insert_position += 1
#         return insert_position



# # And this code is purely mine and it does work, only on non-negative integers.
# # Aparently the "set" only sorts the non-negatives.
nums = [-2, -3, -1,0,0,0,0,3,3]
x = list(set(nums))
del nums[:]
nums.extend(x)
print(nums)