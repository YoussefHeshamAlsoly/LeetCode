# 15. 3Sum
# https://leetcode.com/problems/3sum/description/


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        
        for start in range(len(nums)):
            # no repeated "start"
            if start > 0 and nums[start] == nums[start-1]:
                continue
            
            left = start+1
            right = len(nums) - 1

            while left < right:
                total = nums[start] + nums[left] + nums[right]

                if total < 0: # means we need to get a bigger number, so move "left"
                    left += 1
                elif total > 0: # means we need to get a smaller number, so move "right"
                    right -= 1
                else:
                    res.append([nums[start], nums[left], nums[right]])
                    left += 1

                    # same check for no repeated "start", only now its for "left"
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        
        return res
    
x = Solution()

nums = [-1,0,1,2,-1,-4]
ans = x.threeSum(nums)
print(ans)