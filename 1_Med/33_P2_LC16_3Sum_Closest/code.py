# 16. 3Sum Closest
# https://leetcode.com/problems/3sum-closest/description/


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for start in range(len(nums) - 2):
            if start > 0 and nums[start] == nums[start-1]:
                continue
            
            left = start + 1
            right = len(nums) - 1
            
            while left < right:
                current_sum = nums[start] + nums[left] + nums[right]
                
                if current_sum == target:
                    return current_sum
                
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return closest_sum

x = Solution()

nums = [2, 5, 6, 7]
target = 16
ans = x.threeSumClosest(nums, target)
print(ans)