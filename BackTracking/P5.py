def nQueen(n):
    solution=[]
    pos_diag = set()
    neg_diag = set()
    col = set()
    
    board = [['.']*n for _ in range(n)]
    
    def backTrack(r):
        if r==n:
            copy = [' '.join(row) for row in board]
            solution.append(copy)
            return
        for c in range(n):
            if c in col or r+c in pos_diag or r-c in neg_diag:
                continue
            pos_diag.add(r+c)
            neg_diag.add(r-c)
            col.add(c)
            board[r][c] = 'Q'
            
            backTrack(r+1)
            
            pos_diag.remove(r+c)
            neg_diag.remove(r-c)
            col.remove(c)
            board[r][c] = '.' 
            
    backTrack(0)
    return solution

result = nQueen(4)

for ans in result:
    for an in ans:
        print(an)
    print()