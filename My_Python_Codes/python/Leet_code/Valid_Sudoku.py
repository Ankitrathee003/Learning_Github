
board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]


def get_row(board):
    row={i:board[1][i] for i in range (9) if board[1][i]!='.' }
def get_column(board,j):
    column={i:board[1][i] for i in range (9) if board[1][i]!='.' }
def get_box(board,i,j):
    box={k:board[k][range(j+3)] for k in range (3+j) if board[k]!="."}
    return(box)

print(get_box(board,1,1))


# for i in range (9):
#     for j in range (9):
