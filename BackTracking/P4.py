"""
Problem Description

Given an m × n grid of characters board and a string word, return true if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.

The same letter cell may not be used more than once.

Example 1

Input:

board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
]

word = "ABCCED"

Output:

true
Example 2

Input:

board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
]

word = "SEE"

Output:

true
"""
from collections import Counter
def wordSearch(board,word):
    
    rows = len(board)
    cols = len(board[0])
    
    board_counts = Counter(ch for r in board for ch in r)
    word_counts = Counter(ch for ch in word)
    
    for ch , counts in word_counts.items():
        if board_counts[ch] < counts:
            return False
       
    def backtrack(r,c,index):
        if index == len(word):
            return True
        if r<0 or r>=rows or c<0 or c>=cols or board[r][c] != word[index]:
            return False
        temp = board[r][c]
        board[r][c]='#'
        Found = ( backtrack(r+1,c,index+1) or
                 backtrack(r,c+1,index+1)or
                 backtrack(r-1,c,index+1)or
                 backtrack(r,c-1,index+1) )
        board[r][c]=temp
        return Found
    
    for i in range(rows):
        for j in range(cols):
             if backtrack(i,j,0):
                 return True
    
    return False
        
            

board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
]

word = "ABCCEDF"

print(wordSearch(board,word))