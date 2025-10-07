# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/description/
from itertools import chain

def merge(intervals: list[list[int]]) -> list[list[int]]:
    # My solution
    intervals = sorted(intervals)
    intervals = list(chain.from_iterable(intervals))

    count = 1
    while count < len(intervals)-1:
        if intervals[count] >= intervals[count + 1] and intervals[count] <= intervals[count + 2]:
            del intervals[count:count+2]

        elif intervals[count] >= intervals[count + 1] and intervals[count] > intervals[count + 2]:
            del intervals[count+1:count+3]
        else:
            count += 2
    intervals = [intervals[i:i+2] for i in range(0, len(intervals), 2)]
    return intervals

    # # ChatGPT's solution
    # if not intervals:
    #     return []

    # intervals.sort(key=lambda x: x[0])
    # merged = [intervals[0]]

    # for start, end in intervals[1:]:
    #     last_end = merged[-1][1]

    #     if start <= last_end:
    #         merged[-1][1] = max(last_end, end)
    #     else:
    #         merged.append([start, end])

    # return merged




intervals = [[1,3],[2,6],[8,10],[15,18]]
output = [[1,6],[8,10],[15,18]]
x = merge(intervals)
# print(x)
print(x == output)


intervals = [[4,7],[1,4]]
output = [[1,7]]
x = merge(intervals)
# print(x)
print(x == output)



intervals = [[1,4],[2,3]]
output = [[1,4]]
x = merge(intervals)
# print(x)
print(x == output)


intervals = [[1,4],[0,2],[3,5]]
output = [[0,5]]
x = merge(intervals)
# print(x)
print(x == output)


intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
output = [[1,10]]
x = merge(intervals)
# print(x)
print(x == output)


intervals = [[1,4],[0,2],[3,5]]

output = [[0,5]]
x = merge(intervals)
# print(x)
print(x == output)
