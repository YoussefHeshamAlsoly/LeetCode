# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/description/

def maxArea(height: list[int]) -> int:
    left = 0
    right = len(height) - 1
    max_area = 0
    
    while left < right: #         This part calculates the area (duh)
        max_area = max(max_area, (min(height[left], height[right])*(right - left)))
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1

    return max_area

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))
