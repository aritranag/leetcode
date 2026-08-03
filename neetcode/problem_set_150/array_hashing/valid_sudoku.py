def isValidSudoku(board : list[list[str]]) -> bool:
    # Checking for valid sudoku

    #Column and row check in board
    for i in range(0,9):
        row_set, col_set = set(), set()
        for j in range(0,9):
            # row check
            if board[i][j] != "." and board[i][j] not in row_set:
                row_set.add(board[i][j])
            elif board[i][j] == ".":
                pass
            else:
                #print("Breaking at row",i,j,board[i][j], row_set)
                return False

            # col check
            if board[j][i] != "." and board[j][i] not in col_set:
                col_set.add(board[j][i])
            elif board[j][i] == ".":
                pass
            else:
                #print("Breaking at col",i,j, col_set)
                return False

    # Loop through rows (0,3,6)
    for row_offset in range(0,9,3):
        # Loop through cols (0,3,6)
        for col_offset in range(0,9,3):
            # find each row in the grid
            elem_set = set()
            for i in range(3):
                subgrid_row = board[row_offset+i][col_offset:col_offset+3]
                for elem in subgrid_row:
                    if elem != "." and elem not in elem_set:
                        elem_set.add(elem)
                    elif elem == ".":
                        pass
                    else:
                        #print("Breaking at grid",elem,subgrid_row, elem_set)
                        return False

    return True

# TODO : write the bitmask solution


board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))

