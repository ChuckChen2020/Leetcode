# 2021 May 17 13:19 - 13:55
from typing import List, Set, Tuple
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        def check_level(r, c, lvl):
            RS, CS = r + lvl, c + lvl
            for cc in range(c, CS + 1):
                if matrix[RS][cc] == "0":
                    return lvl
            for rr in range(r, RS):
                if matrix[rr][CS] == "0":
                    return lvl
            # At every level, if it fails the function passes back the last
            # level, which was fulfilled. In this case, there's no next
            # level, but the current is fulfilled. So it returns the
            # fulfilled level, lvl + 1, without calling the check for next.
            if RS == ROWS - 1 or CS == COLS - 1:
                return lvl + 1
            return check_level(r,c, lvl+1)

        max_area = 0
        for row in range(ROWS):
            for col in range(COLS):
                level = check_level(row, col, 0)
                max_area = max(max_area, level*level)
        return max_area

if __name__ == "__main__":
    print(Solution().maximalSquare([["0"]]))