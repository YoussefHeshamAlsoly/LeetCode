# 75. Sort Colors
# https://leetcode.com/problems/sort-colors/description/




RED = "\033[31m"
GREEN = "\033[32m"
END = "\033[0m"

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for p1 in range(len(nums)):
            for p2 in range(p1+1, len(nums)):
                if nums[p1]>nums[p2]:
                    nums[p1], nums[p2] = nums[p2], nums[p1]

