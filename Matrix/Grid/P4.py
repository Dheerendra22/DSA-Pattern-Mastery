"""
Problem Description

Given an m × n matrix, return all elements of the matrix in spiral order.

Starting from the top-left corner, the order of traversal should be:

Move from left to right across the current top row.
Move from top to bottom along the current rightmost column.
Move from right to left across the current bottom row (if applicable).
Move from bottom to top along the current leftmost column (if applicable).
Repeat the process for the inner boundaries until all elements are visited.
Examples
Example 1:

Input:

matrix = [[1,2,3],[4,5,6],[7,8,9]]

Output:

[1,2,3,6,9,8,7,4,5]

Visual:

1 → 2 → 3
          ↓
4 → 5    6
↑         ↓
7 ← 8 ←  9

So the spiral traversal is:

1 → 2 → 3 → 6 → 9 → 8 → 7 → 4 → 5
"""
def printSpiral(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    result = []

    # right, down, left, up
    directions = [
        [0, 1],
        [1, 0],
        [0, -1],
        [-1, 0]
    ]

    nr, nc = 0, 0
    direction = 0

    for _ in range(rows * cols):

        # 1. Visit current cell
        result.append(matrix[nr][nc])

        # 2. Mark current cell as visited
        matrix[nr][nc] = '*'

        # 3. Calculate next position
        next_r = nr + directions[direction][0]
        next_c = nc + directions[direction][1]

        # 4. If next position is invalid/visited,
        #    turn clockwise
        if (next_r < 0 or next_r >= rows or
            next_c < 0 or next_c >= cols or
            matrix[next_r][next_c] == '*'):

            direction = (direction + 1) % 4

            next_r = nr + directions[direction][0]
            next_c = nc + directions[direction][1]

        # 5. Move
        nr = next_r
        nc = next_c

    return result


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# print(printSpiral(matrix))

# Another way to easily understand !!
def spiral(matrix):
    if not matrix or not matrix[0]:
        return []
    result=[]
    top,bottom=0,len(matrix)-1
    left,right=0,len(matrix[0])-1

    while top<=bottom and left<=right:
        for i in range(left,right+1):
            result.append(matrix[top][i])
        top+=1

        for i in range(top,bottom+1):
            result.append(matrix[i][right])
        right-=1

        if top<=bottom:
            for i in range(right,left-1,-1):
                result.append(matrix[bottom][i])
            bottom-=1

        if left<=right:
            for i in range(bottom,top-1,-1):
                result.append(matrix[i][left])
            left+=1
    return result 

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(spiral(matrix))
