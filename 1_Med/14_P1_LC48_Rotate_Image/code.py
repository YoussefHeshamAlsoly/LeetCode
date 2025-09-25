# 48. Rotate Image
# https://leetcode.com/problems/rotate-image/description/

# Recommended (the standard solution): Transpose + Reverse (simple, clean, in-place, O(1) extra)

# def rotate(matrix: list[list[int]]) -> None:
#     n = len(matrix)
#     # transpose
#     for i in range(n):
#         for j in range(i + 1, n):
#             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#     # reverse each row
#     for i in range(n):
#         matrix[i].reverse()




def rotate(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    log = set()
    for i in range(int(n)):
        for j in range(int(n)):
            if (i,j) in log: # That extra "," was ESSENTIAL
                continue
            else:
                matrix[i][j], matrix[j][n-1-i] = matrix[j][n-1-i], matrix[i][j]
                log.add((j, len(matrix)-1-i))

matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)
print(matrix == [[7,4,1],[8,5,2],[9,6,3]])



matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
rotate(matrix)
print(matrix == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])
