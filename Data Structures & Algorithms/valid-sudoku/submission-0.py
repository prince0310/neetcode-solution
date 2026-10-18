class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row check 
        
        for row_num in range(9):
            temp = {}
            for index in range(9):
                if board[row_num][index] == ".":
                    continue
                elif board[row_num][index] not in temp:
                    temp[board[row_num][index]] = 1
                else:
                    return False
        # column check
        for col_num in range(9):
            temp = {}
            for index in range(9):
                if board[index][col_num] == ".":
                    continue
                elif board[index][col_num] not in temp:
                    temp[board[index][col_num]] = 1
                else:
                    return False

        def check3x3(start_row, start_column):
            temp = {}
            for i in range(start_row, start_row+3):
                for j in range(start_column, start_column+3):
                    if board[i][j] == ".":
                        continue
                    elif board[i][j] not in temp:
                        temp[board[i][j]] = 1
                    else:
                        return False
            return True

        for i in range(3):
            for j in range(3):
                if check3x3(3*i, 3*j) :
                    continue 
                else:
                    return False

        return True




        