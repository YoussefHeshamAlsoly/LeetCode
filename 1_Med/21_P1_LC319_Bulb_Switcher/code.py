# 319. Bulb Switcher
# https://leetcode.com/problems/bulb-switcher/description/

class Solution:
    def bulbSwitch(self, n: int) -> int:
        # Solution 1
        # left, right = 0, n
        # while left<=right:
        #     middle = left + (right - left)//2
        #     square = middle * middle
        #     if square == n:
        #         return (middle)
        #     elif square < n:
        #         left = middle + 1
        #     else:
        #         right = middle - 1
        # return int(right)

        # Solution 2
        # from math import sqrt
        # return int(sqrt(n))

        # Solution 3
        return int(n**(1/2))