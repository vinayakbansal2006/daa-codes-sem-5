
#n-queen
def solve(row, board, n):
    if row == n:
        for r in range(n):
            print("Row:", r, "Column:", board[r])
        print()
        return

    for col in range(n):
        safe = True

        for r in range(row):
            if board[r] == col or abs(row-r) == abs(col-board[r]):
                safe = False
                break

        if safe:
            board[row] = col
            solve(row+1, board, n)
            board[row] = -1

n = 4
board = [-1] * n
solve(0, board, n)
