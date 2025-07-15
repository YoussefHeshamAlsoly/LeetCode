def transpose(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[List[int]]
    """
    # m, n = len(matrix), len(matrix[0])
    # res = [[0] * m for _ in range(n)]
    # # res = matrix[:]
    # for i, j in enumerate(matrix):
    #     for x, y in enumerate(j):
    #         print(f"i: {i}, x: {x}, y: {y}")
    #         res[x][i] = matrix[i][x]
    #         # print(res)
    
    return [list(row) for row in zip(*matrix)]

# matrix = [[1,2,3],[4,5,6],[7,8,9]]

matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]
print(transpose(transpose(matrix))==matrix)