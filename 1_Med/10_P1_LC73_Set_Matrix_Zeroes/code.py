# 73. Set Matrix Zeroes
# https://leetcode.com/problems/set-matrix-zeroes/description/

def setZeroes(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    rows = set()
    cols = set()

    for row in range(len(matrix)):
        for cell in range(len(matrix[row])):
            if matrix[row][cell] == 0:
                rows.add(row)
                cols.add(cell)

    for row in range(len(matrix)):
        for cell in range(len(matrix[row])):
            if row in rows or cell in cols:
                matrix[row][cell] = 0

    # ===========================================================================================================
    # Assistant's code
    # rows = len(matrix)
    # cols = len(matrix[0])

    # # Determine if the first row and first column need to be zeroed out
    # first_row_has_zero = any(matrix[0][col] == 0 for col in range(cols))
    # first_col_has_zero = any(matrix[row][0] == 0 for row in range(rows))

    # # Use the first row and first column as markers
    # for row in range(1, rows):
    #     for col in range(1, cols):
    #         if matrix[row][col] == 0:
    #             matrix[row][0] = 0
    #             matrix[0][col] = 0

    # # Zero out the rest of the matrix based on markers
    # for row in range(1, rows):
    #     for col in range(1, cols):
    #         if matrix[row][0] == 0 or matrix[0][col] == 0:
    #             matrix[row][col] = 0

    # # Zero out the first row if needed
    # if first_row_has_zero:
    #     for col in range(cols):
    #         matrix[0][col] = 0

    # # Zero out the first column if needed
    # if first_col_has_zero:
    #     for row in range(rows):
    #         matrix[row][0] = 0






# matrix = [
#         [1,1,1],
#         [1,0,1],
#         [1,1,1]
#         ]
# print (matrix)
# setZeroes(matrix)
# print (matrix == [[1,0,1],[0,0,0],[1,0,1]])


matrix = [
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]
    ]
setZeroes(matrix)
print(matrix)

print(matrix == [[0,0,0,0],[0,4,5,0],[0,3,1,0]])