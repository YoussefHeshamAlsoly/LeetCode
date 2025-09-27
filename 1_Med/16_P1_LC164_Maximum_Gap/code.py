# 164. Maximum Gap
# https://leetcode.com/problems/maximum-gap/description/


# Not really solved. The runtime is not linear. Its O(NlogN)
def maximumGap(nums: list[int]) -> int:
    if len(nums)<2:
        return 0
    
    nums = sorted(nums)
    MAX = -0
    for i in range(1, len(nums)):
        MAX = max(nums[i] - nums[i-1], MAX)
    return MAX

nums = [10]
print(maximumGap(nums))