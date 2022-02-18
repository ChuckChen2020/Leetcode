# 2021 May 11, 23:14 -00:09
from typing import List, Set, Tuple
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        level = 1
        while True:
            updated = False
            for r in range(ROWS):
                for c in range(COLS):
                    up = level if r == 0 else mat[r-1][c]
                    down = level if r == ROWS - 1 else mat[r+1][c]
                    left = level if c == 0 else mat[r][c-1] 
                    right = level if c == COLS - 1 else mat[r][c+1]
                    if up >= level and down >= level and left >= level and right >= level and mat[r][c] >= level:
                        mat[r][c] += 1
                        updated = True
            if not updated: break
            level += 1

        return mat

if __name__ == "__main__":
    print(Solution().updateMatrix([[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]]))