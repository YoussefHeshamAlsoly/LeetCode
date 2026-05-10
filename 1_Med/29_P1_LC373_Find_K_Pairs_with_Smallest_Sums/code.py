# # 373. Find K Pairs with Smallest Sums
# # https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/


from heapq import heappush, heappop
def kSmallestPairs(nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
    res = []
    m, n, visited = len(nums1), len(nums2), set()

    h = [(nums1[0]+nums2[0], (0, 0))]

    for _ in range(min(k, (m*n))):
        val, (i, j) = heappop(h)
        res.append([nums1[i], nums2[j]])
        
        if i+1 < m and (i+1, j) not in visited:
            heappush(h, (nums1[i+1]+nums2[j], (i+1, j)))
            visited.add((i+1, j))
        
        if j+1 < n and (i, j+1) not in visited:
            heappush(h, (nums1[i]+nums2[j+1], (i, j+1)))
            visited.add((i, j+1))
    return res



nums1 = [1,1,2]
nums2 = [1,2,3]
k = 3
print(kSmallestPairs(nums1, nums2, k))