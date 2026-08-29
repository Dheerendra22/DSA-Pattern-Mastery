"""
Problem Description
Given an n × n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.
A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All adjacent cells of the path are 8-directionally connected (up, down, left, right, and the four diagonals).
The length of a clear path is the number of visited cells in this path.
Examples
Example 1
0  1
1  0
Input:
grid = [[0,1],[1,0]]
Output:
2
Explanation: The path is:
(0,0) → (1,1)
Example 2
0  0  0
1  1  0
1  1  0
Input:
grid = [[0,0,0],[1,1,0],[1,1,0]]
Output:
4
Explanation: The path is:
(0,0) → (0,1) → (1,2) → (2,2)

"""

from collections import deque
def shortestPath(grid):  # using BFS 
    n=len(grid)
    if grid[0][0]==1 or grid[n-1][n-1]==1:
        return -1
    if n==1:
        return 1
    
    directions=[
        (-1,1),
        (0,1),
        (1,-1),(1,0),(1,1)
    ]
    queue=deque([(0,0,1)])
    grid[0][0]=1

    while queue:
        r,c,length=queue.popleft()

        for dr,dc in directions:
            nr,nc=r+dr,c+dc 

            if 0<=nr<n and 0<=nc<n and grid[nr][nc]==0:
                if nr==n-1 and nc==n-1:  # if last lastcell of grid
                    return length+1
                grid[nr][nc]=1
                queue.append((nr,nc,length+1))
    return -1

print(shortestPath( [[0,0,0],[1,1,0],[1,1,0]]))