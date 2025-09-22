# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

def findKthLargest(nums: list[int], k: int) -> int:
    # Method 1: Too slow for large lists
    # for i in range(k-1):
    #     nums.pop(nums.index(max(nums)))
    # return max(nums)


    # Method 2: LC does not want to use "sort"
    # nums = sorted(nums, reverse=True)
    # return nums[k-1]
    # return sorted(nums, reverse=True)[k-1]


    # Method 3: working. new concept. HEAP.
    import heapq
    heapq.heapify(nums)
    return heapq.nlargest(k, nums)[-1]


# nums = [3,2,1,5,6,4]
# k = 2
# print(findKthLargest(nums, k) == 5)


# nums = [3,2,3,1,2,4,5,5,6]
# k = 4
# print(findKthLargest(nums, k) == 4)


