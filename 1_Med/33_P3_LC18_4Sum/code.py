# 18. 4Sum
# https://leetcode.com/problems/4sum/description/


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                            
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        
        return res
    

x = Solution()

list_of_nums = [
        [1,0,-1,0,-2,2],
        [2,2,2,2,2],
        [-3,-1,0,2,4,5],
        [-3,-2,-1,0,0,1,2,3]
    ]

list_of_targets = [
        0,
        8,
        0,
        0
    ]

list_of_answers = [
        [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]],
        [[2,2,2,2]],
        [[-3,-1,0,4]],
        [[-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    ]

for i in range (len(list_of_nums)):
    print('\n\n')
    ans = x.fourSum(list_of_nums[i], list_of_targets[i])
    print("sorted nums:   ", sorted(list_of_nums[i]))
    print("my answer:     ", ans)
    print("actual answer: ", list_of_answers[i])
    print(ans == list_of_answers[i])


'''
my answer:      [[-3, -2, 2, 3], [-3, -1, 1, 3], [-3, 0, 0, 3], [-3, 0, 1, 2], [-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
actual answer:  [[-3, -2, 2, 3], [-3, -1, 1, 3], [-3, 0, 0, 3], [-3, 0, 1, 2], [-2, -1, 0, 3], [-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

'''