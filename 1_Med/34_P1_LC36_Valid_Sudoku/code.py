# 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/description/

RED = "\033[31m"
GREEN = "\033[32m"
END = "\033[0m"



class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        col = 0
        current_col = []
        main_corners = [[0,0], [0,3], [0,6],
                        [3,0], [3,3], [3,6],
                        [6,0], [6,3], [6,6]
                        ]

        # process rows
        for row in board: # row is a list of all elements in a row
            current_row = [i for i in row if i != "."]
            if len(current_row) != len(set(current_row)): # no duplicates
                # print(f"{RED}Failed in rows{END}")
                return False
        
        # process columns
        for row in range(len(board)):
            for cell in range(len(board)): # it is a square so it doesn't matter the exact range formula
                current_col.append(board[cell][col])
            
            
            current_col = [i for i in current_col if i != "."]
            if len(current_col) != len(set(current_col)): # no duplicates
                # print(f"{RED}Failed in columns{END}")
                return False
            col += 1
            current_col = []

        # process squares
        for row,col in main_corners:
            square = [  
                        board[row][col], board[row][col+1], board[row][col+2],
                        board[row+1][col], board[row+1][col+1], board[row+1][col+2],
                        board[row+2][col], board[row+2][col+1], board[row+2][col+2]
                    ]
            square = [i for i in square if i != "."]
            if len(square) != len(set(square)):
                # print(f"{RED}Failed in squares{END}")
                return False

        return True


boards = [

            [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]],

            [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]],
]

actual_answers = [
    True,
    False
]

x = Solution()


for i in range(len(boards)):
    my_answer = x.isValidSudoku(boards[i])
    if my_answer == actual_answers[i]:
        print(f"{GREEN}test case {i+1}: Pass{END}")
    else:
        # print(f"{RED}test case {i+1}: Fail{END}")
        pass

