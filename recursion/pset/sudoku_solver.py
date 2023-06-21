def solve_sudoku_puzzle(board):
    helper(board)
    return board


def helper(board):
    # get row with first empty entry
    row = 0
    while get_empty_in_row(board[row]) == -1:
        row += 1
        # if no empty entries, board is solved
        if row == 9:
            return True

    # get col of empty entry in that row
    col = get_empty_in_row(board[row])

    # try integers 1,9 in entry at location (row,col)
    for i in range(1, 10):
        if is_safe(board, row, col, i):
            board[row][col] = i

            # if chosing i for this entry works recursiveley throughout solving the rest of
            # the board, then this is a valid partial solution!
            if helper(board):
                return True
            else:
                # if its not, undo our change and continue with other values (i.e., backtrack)
                board[row][col] = 0

    # no entry was valid for (row,col) so we "bubble up" to previous choice that led us astray
    return False


# index function throws ValueError 🙄
def get_empty_in_row(row):
    i = None
    try:
        i = row.index(0)
    except:
        i = -1
    return i


# determines weather board is a valid sudoku solution if val is entered at (row,col)
def is_safe(board, r, c, val):
    # row violation
    if val in board[r]:
        return False

    # column violation
    for i in range(9):
        if val == board[i][c]:
            return False

    # start row/col of 3x3 subgrid for entry at (row,col)
    start_r = r - r % 3
    start_c = c - c % 3

    # 3x3 subgrid violation
    for i in range(3):
        for j in range(3):
            if board[start_r + i][start_c + j] == val:
                return False

    # all requirements are satisfied, so we are left with a valid sudoku solution.
    return True


ex = [
    [8, 4, 9, 0, 0, 3, 5, 7, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0],
    [7, 0, 0, 0, 9, 0, 0, 8, 3],
    [0, 0, 0, 9, 4, 6, 7, 0, 0],
    [0, 8, 0, 0, 5, 0, 0, 4, 0],
    [0, 0, 6, 8, 7, 2, 0, 0, 0],
    [5, 7, 0, 0, 1, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 2, 1, 7, 0, 0, 8, 6, 5],
]

ans = [
    [8, 4, 9, 1, 6, 3, 5, 7, 2],
    [3, 1, 5, 2, 8, 7, 4, 9, 6],
    [7, 6, 2, 4, 9, 5, 1, 8, 3],
    [1, 5, 3, 9, 4, 6, 7, 2, 8],
    [2, 8, 7, 3, 5, 1, 6, 4, 9],
    [4, 9, 6, 8, 7, 2, 3, 5, 1],
    [5, 7, 8, 6, 1, 9, 2, 3, 4],
    [6, 3, 4, 5, 2, 8, 9, 1, 7],
    [9, 2, 1, 7, 3, 4, 8, 6, 5],
]

print(solve_sudoku_puzzle(ex) == ans)
