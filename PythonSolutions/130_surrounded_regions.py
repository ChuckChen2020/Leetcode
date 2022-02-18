# 2021 May 6 21:49 - 22:29
from typing import List, Set, Tuple
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        d = (-1,0,1,0,-1)
        visited_all = set()

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O" and row not in (0, ROWS - 1) and col not in (0, COLS - 1) and (row, col) not in visited_all:
                    flip = True
                    stack = [(row, col)]
                    visited = set()

                    while len(stack) != 0:
                        r, c = stack.pop()
                        visited.add((r,c)) 
                        for i in range(4):
                            x, y = r + d[i], c + d[i+1]
                            if x not in (-1, ROWS) and y not in (-1, COLS) and board[x][y] == "O" and (x,y) not in visited:
                                stack.append((x,y))
                                if x in (0, ROWS-1) or y in (0, COLS-1):
                                    flip = False
                                
                    if flip:
                        for r,c in visited:
                            board[r][c] = "X"
                    visited_all.union(visited)


if __name__ == "__main__":
    board = [["X","X","X"],["X","O","X"],["X","X","X"]]
    Solution().solve(board)
    print(board)