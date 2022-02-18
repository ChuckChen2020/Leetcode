# 2021 May 11, 20:50 - 23:00
from sys import maxsize
from typing import List, Set, Tuple
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = [[0 for col in range(COLS)] for row in range(ROWS)]
        dp[0][0] = grid[0][0]

        # At every node, the incoming route could only come through either the node above, or the node left (Fortunately, detour from right and down nodes are not allowed, otherwise it can get really complicated, as it's possible that such detours can be legitimatelly taken).  
        for r in range(0, ROWS):
            for c in range(0, COLS):
                if r == 0 and c == 0: continue
                dp[r][c] = min(maxsize if r == 0 else dp[r-1][c], maxsize if c == 0 else dp[r][c-1]) + grid[r][c]
        
        return dp[-1][-1]



        

if __name__ == "__main__":
    print(Solution().minPathSum([[1,4,7,2],[93,96,1,5],[8,1,1,1],[4,2,9,3]]))