# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

def search(nums: list[int], target: int) -> int:
    left_ptr = 0
    right_ptr = len(nums) - 1

    while left_ptr <= right_ptr:
        mid_ptr = (right_ptr + left_ptr) // 2
        
        if nums[mid_ptr] == target:
            return mid_ptr
        
        if nums[left_ptr] <= nums[mid_ptr]:
            if nums[left_ptr] <= target < nums[mid_ptr]:
                right_ptr = mid_ptr - 1
            else:
                left_ptr = mid_ptr + 1
        
        else:
            if nums[mid_ptr] < target <= nums[right_ptr]:
                left_ptr = mid_ptr + 1
            else:
                right_ptr = mid_ptr - 1


    return -1

nums = [4,5,6,7,0,1,2]
target = 0
print(search(nums, target)==4)


nums = [4,5,6,7,0,1,2]
target = 3
print(search(nums, target)==-1)

nums = [1]
target = 0
print(search(nums, target)==-1)
