# 442. Find All Duplicates in an Array
# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
from collections import Counter

def findDuplicates(nums: list[int]) -> list[int]:
    # ChatGPT's code
    seen = set()
    duplicates = set()
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)
    
    # # My code. its better btw
    # return [i[0] for i in Counter(nums).items() if i[1] == 2]

nums1 = [4,3,2,7,8,2,3,1]
ans1 = [2,3]
acc_ans1 = findDuplicates(nums1)
print(f"res: {acc_ans1}")
print(acc_ans1 == ans1)
print()

nums2 = [1,1,2]
ans2 = [1]
acc_ans2 = findDuplicates(nums2)
print(f"res: {acc_ans2}")
print(acc_ans2 == ans2)
print()

nums3 = [1]
ans3 = []
acc_ans3 = findDuplicates(nums3)
print(f"res: {acc_ans3}")
print(acc_ans3 == ans3)
print()
