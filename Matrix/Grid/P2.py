"""
Problem Description
Given an m x n binary matrix filled with 0s and 1s, find the largest square containing only 1s and return its area.
Example 1
Input:
matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]
Output:
4
Explanation:
The largest square has a side length of 2.
Therefore:
Area = side × side
     = 2 × 2
     = 4
Example 2
Input:
matrix = [
    ["0","1"],
    ["1","0"]
]
Output:
1
Because there is no 2 × 2 square containing only 1s. The largest possible square is:
1 × 1
So:
Area = 1 × 1 = 1
"""
def solution(matrix):
    if not matrix or not matrix[0]:
        return 0
    rows,cols=len(matrix),len(matrix[0])
    dp=[0]*(cols+1) 
    max_side=0
    prev=0

    for i in range(1,rows+1):
        for j in range(1,cols+1):
            temp=dp[j]

            if matrix[i-1][j-1]=='1':
                dp[j]=min(dp[j],dp[j-1],prev)+1
                max_side=max(max_side,dp[j])

            else:
                dp[j]=0
            prev=temp 
    return max_side*max_side

matrix=[
    ['1','0','1','0','0'],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"], 
    ["1","0","0","1","0"]
]
print(solution(matrix))