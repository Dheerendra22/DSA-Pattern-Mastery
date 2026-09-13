"""
Value	Meaning
0	Originally dead → stays dead
1	Originally alive → stays alive
2	Originally alive → will die
3	Originally dead → will become alive
"""


def solution(board):

    # Handle empty board
    if not board or not board[0]:
        return

    rows = len(board)
    cols = len(board[0])

    # --------------------------------------------------
    # STEP 1: Calculate the next state for every cell
    # --------------------------------------------------

    for r in range(rows):
        for c in range(cols):

            live_neighbors = 0

            # Check all 8 neighboring cells
            for i in range(max(0, r - 1), min(rows, r + 2)):
                for j in range(max(0, c - 1), min(cols, c + 2)):

                    # Don't count the current cell
                    if i == r and j == c:
                        continue

                    # 1 = currently alive
                    # 2 = currently alive, but will die
                    if board[i][j] == 1 or board[i][j] == 2:
                        live_neighbors += 1

            # --------------------------------------------------
            # STEP 2: Decide whether the current cell changes
            # --------------------------------------------------

            if board[r][c] == 1:

                # Alive cell dies if:
                #   - fewer than 2 neighbors
                #   - more than 3 neighbors
                if live_neighbors < 2 or live_neighbors > 3:
                    board[r][c] = 2

            else:

                # Dead cell becomes alive if exactly 3 neighbors
                if live_neighbors == 3:
                    board[r][c] = 3

    # --------------------------------------------------
    # STEP 3: Convert temporary states into final states
    # --------------------------------------------------

    for r in range(rows):
        for c in range(cols):

            if board[r][c] == 2:
                # Was alive → now dead
                board[r][c] = 0

            elif board[r][c] == 3:
                # Was dead → now alive
                board[r][c] = 1