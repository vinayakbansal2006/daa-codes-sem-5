
#n-queen
def solve(row,board,n):
    if row ==n:
        for r in range(n):
            print("row ",r,"col ",board[r])
        