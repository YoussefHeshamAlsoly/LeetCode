from collections import Counter
def intersect(nums1:list, nums2:list):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    nums1 = Counter(nums1)
    nums2 = Counter(nums2)
    res = []
    for i in nums1.keys():
        res.extend([i for _ in range(min(nums1[i], nums2[i]))])

    return res

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

print(intersect(nums1, nums2))



# this implementation is iterating over the shortest given list
"""
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    c1 = Counter(nums1)
    res = []

    for num in nums2:
        if c1[num] > 0:
            res.append(num)
            c1[num] -= 1

    return res
"""