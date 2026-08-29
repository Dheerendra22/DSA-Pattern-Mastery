""""
Problem Description
Given an m * n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are surrounded by water.
Example 1
Input:
grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
Output:
1
"""
from collections import deque 

def findIsland(grid): #using BFS
    if not grid:
        return 0
    rows,cols=len(grid), len(grid[0])
    island=0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c]=="1":
                island+=1
                queue=deque([(r,c)])
                grid[r][c]="0"

                while queue:
                 row,col=queue.popleft()
                 for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                     nr,nc=row+dr,col+dc 
                     if (0<=nr<rows and 0<=nc<cols and grid[nr][nc]=="1"):
                         queue.append((nr,nc))
                         grid[nr][nc]="0"
    return island      
g = [
["1","1","1","1","0"],
["1","1","0","0","1"],
["1","1","0","0","0"],
["0","0","0","1","1"]
]
print(findIsland(g))

"""
Go through every cell.

If I find a "1":
    I found a NEW island.
    Increase island count.

    Put this cell into a queue.
    Mark it as visited.

    While there are cells in the queue:
        Take one cell.

        Check:
            DOWN
            UP
            RIGHT
            LEFT

        If the neighbor:
            is inside the grid
            AND is "1":

                Put it into the queue.
                Mark it as visited.

Continue scanning the grid.

Return the number of islands.
"""