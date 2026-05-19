# 57. Insert Interval
# https://leetcode.com/problems/insert-interval/description/




RED = "\033[31m"
GREEN = "\033[32m"
END = "\033[0m"

class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        intervals.append(newInterval)
        intervals.sort()

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            if res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])

        return res



intervals = [
    [[1,3],[6,9]],
    [[1,2],[3,5],[6,7],[8,10],[12,16]]
]

newInterval = [
    [2,5],
    [4,8]
]

Output = [
    [[1,5],[6,9]],
    [[1,2],[3,10],[12,16]]
]


x = Solution()

for iter in range (len(intervals)):
    print('\n')
    ans = x.insert(intervals[iter], newInterval[iter])
    print("My answer:     ", ans)
    print("Actual answer: ", sorted(Output[iter]))
    if ans == Output[iter]:
        print(f"Verdict:        {GREEN}Pass{END}")
    else:
        print(f"Verdict:        {RED}Fail{END}")