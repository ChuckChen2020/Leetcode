# 2021 May 23 17:36 - surrendered
#   "coin", "change"
#   i ->
#   coin
#   j ->
#   change
#   c is the same for i, j pointers, so dp[coin][change] = dp[oin][hange]
#   o, h are different. In such case, we can choose to do in 1 op:
#   1)  insert: would want to insert h, than we start to compare o to a. 
#       (j switch to next).
#   2)  delete: would want to delete o, than we compare i to h. (i to next)
#   3)  replace: would want to replace o with h. i, j both switch to next.
#   So, in pointers' term, when word[i] != word[j], if dp denotes number of #   ops it takes,
#   dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1]).
#   Boundary conditions come from the bottom and right sides: 
#   "coin" to ""? 4, "oin" to ""? 3, ......
#   Solution is updated bottom-up. 
#   dp      c       o       i       n       " "
#   c      (4)      5       5       5       6
#   h       5       4       4       4       5
#   a       4       4       3       3       4
#   n       4       3       3       2       3
#   g       4       3       2       2       2
#   e       4       3       2       1       1
#   ""      4       3       2       1       0
from typing import List, Set, Tuple
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float('inf')] * (len(word1) + 1) for _ in range(len(word2) + 1)]
        for row in range(len(word2) + 1):
            dp[row][len(word1)] = len(word2) - row
        for col in range(len(word1) + 1):
            dp[len(word2)][col] = len(word1) - col
        for row in range(len(word2) - 1, -1, -1):
            for col in range(len(word1) - 1, -1, -1):
                if word1[col] == word2[row]:
                    dp[row][col] = dp[row+1][col+1]
                else:
                    dp[row][col] = 1 + min(dp[row+1][col], dp[row][col+1], dp[row+1][col+1])
        return dp[0][0]

# Focus on the basic cases when performing analysis! Complex cases could 
# easily distract you from gaining insights with the interplay of its
# complexities. Start patiently with the simplest cases!

# DFS + cache can work it out easily. Without caching, it will run into TLE.
from functools import lru_cache
class Solution1:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(maxsize=None)
        def dfs(i, j):
            if i == len(word1) or j == len(word2):
                return max(len(word1) - i, len(word2) - j)
            if word1[i] == word2[j]:
                return dfs(i+1, j+1)
            else:
                return 1 + min(dfs(i+1, j), dfs(i+1, j+1), dfs(i, j+1))

        return dfs(0,0)


if __name__ == "__main__":
    print(Solution1().minDistance("coin", "change"))