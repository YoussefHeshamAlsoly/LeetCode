# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/description/

# def maxSubArray(nums: list[int]) -> int:
#     l_ptr = 0
#     r_ptr = 1
#     max_sum = -1

#     while r_ptr <= len(nums)+1 and l_ptr <= len(nums)+1:
        
#         current_sum = sum(nums[l_ptr:r_ptr+1])

#         if max_sum > current_sum:
#             if r_ptr > l_ptr + 1:
#                 r_ptr += 1
#             else:
#                 l_ptr += 1
        
#         else:
#             max_sum = max(max_sum, current_sum)
#             r_ptr += 1
    
#     return max_sum




# def maxSubArray(nums: list[int]) -> int:
#     maxSum = nums[0]
#     currentSum = nums[0]

#     for num in nums[1:]:
#         currentSum = max(num, currentSum + num)
#         maxSum = max(maxSum, currentSum)

#     return maxSum


def maxSubArray(nums: list[int]) -> int:
    if not nums:
        return 0  # Handle the edge case of an empty list

    max_sum = nums[0]
    current_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

nums = [5,4,-1,7,8]
nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [1]
print(maxSubArray(nums))