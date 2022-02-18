# 2021 May 25, 14:09 - 15:41
# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#         def lcs(i, j, last_j):
#             if i == len(word1):
#                 return 0
#             if j == len(word2):
#                 return lcs(i+1, last_j + 1, last_j)
#             if word1[i] == word2[j]:
#                 print("pair found: ", i, j)
#                 return 1 + lcs(i+1, j+1, j)
#             else:
#                 return lcs(i, j + 1, last_j)         
#         max_lcs = 0
#         for i in range(len(word1)):
#             print(word1[i])
#             max_lcs = max(max_lcs, lcs(i, 0, -1))
#         return len(word1) + len(word2) - 2* max_lcs

class Solution:
    def minDistance(self, word1: str, word2: str) -> int: 
        dp = [[0]*(len(word2) + 1) for _ in range(len(word1) + 1)]

        for row in range(len(word1) - 1, -1, -1):
            for col in range(len(word2) - 1, -1, -1):
                if word1[row] == word2[col]:
                    dp[row][col] = 1 + dp[row + 1][col + 1]
                else:
                    # Got stuck with this part initially.
                    dp[row][col] = max(dp[row][col+1], dp[row+1][col])
        return len(word1) + len(word2) - 2*dp[0][0]

# Try to do the lcs part using top-down memoization.
from functools import lru_cache                       
class Solution1:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(maxsize=None) 
        def lcs(i, j):
            if i == len(word1):
                return 0
            if j == len(word2):
                return 0
            if word1[i] == word2[j]:
                return 1 + lcs(i+1, j+1)
            else:
                return max(lcs(i, j + 1), lcs(i + 1, j)) 
        return len(word1) + len(word2) - 2*lcs(0,0)

if __name__ == "__main__":
    print(Solution1().minDistance("sea","eat"))
    print(Solution1().minDistance("leetcode","etco"))
    print(Solution1().minDistance("testcaseruncode", "resultdebugger"))