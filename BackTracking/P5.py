"""
N-Queens Problem
Problem Description

The n-queens puzzle is the problem of placing n queens on an n × n chessboard such that no two queens attack each other.

Two queens attack each other if they share the same row, column, or diagonal.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1

Input:

n = 4

Output:

[
  [".Q..", "...Q", "Q...", "..Q."],
  ["..Q.", "Q...", "...Q", ".Q.."]
]

Explanation:

There exist two distinct solutions to the 4-queens puzzle as shown above.
"""

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