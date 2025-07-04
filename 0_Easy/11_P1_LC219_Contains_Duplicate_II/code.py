# My code, with time complexity of O(n^2)
# It breaks at 54500 elements and k=35000

# def containsNearbyDuplicate(nums, k):
#     counter = 0
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             counter+=1
#             if counter>k:
#                 counter = 0
#                 break

#             if nums[i] == nums[j]:
#                 return True
#     return False



# Runtime: 28ms Beats 74.33%
# Memory: 23.86MB Beats 65.75%
# ChatGPT's "Hash" code with time complexity of O(n)

def containsNearbyDuplicate(nums, k):
    num_indices = {}
    
    for i, num in enumerate(nums):
        if num in num_indices and i - num_indices[num] <= k:
            return True
        num_indices[num] = i
    
    return False



# Runtime: 55ms Beats 23.16%
# Memory: 24.51MB Beats 41.79%
# This is also ChatGPT's suggestion, this time using sets instead of hashs

# def containsNearbyDuplicate(self, nums, k):
#     """
#     :type nums: List[int]
#     :type k: int
#     :rtype: bool
#     """
#     num_indices = set()
    
#     for i, num in enumerate(nums):
#         if num in num_indices:
#             return True
        
#         num_indices.add(num)
        
#         if len(num_indices) > k:
#             num_indices.remove(nums[i - k])
    
#     return False