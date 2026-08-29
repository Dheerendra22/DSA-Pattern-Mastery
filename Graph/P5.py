from collections import deque 
def RotenOranges(grid):
    if not grid:
        return 0
    rows,cols=len(grid),len(grid[0])
    queue=deque()
    fresh_count=0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c]==2:
                queue.append((r,c,0))
            elif grid[r][c]==1:
                fresh_count+=1
    if fresh_count==0:
        return 0
    minutes_elapsed=0
    directions=[(0,1),(0,-1),(1,0),(-1,0)]

    while queue:
        r,c,minutes=queue.popleft()
        minutes_elapsed=minutes
        for dr,dc in directions:
            nr,nc=r+dr,c+dc 

            if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                grid[nr][nc]=2
                fresh_count-=1
                queue.append((nr,nc,minutes+1))
    return minutes_elapsed if fresh_count==0 else -1

g=[[2,1,1],[1,1,0],[0,1,1]]
print(RotenOranges(g))
