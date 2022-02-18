# 2021 May 15 18:52 - 20:35
from typing import List, Set, Tuple
from math import sqrt
from sys import maxsize
# TLE
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]*(n + 1)
        dp[0] = 0
        for num in range(1, n + 1):
            sr = int(sqrt(num))
            if sr*sr == num:
                dp[num] = 1
                continue
            sol = maxsize
            for a in range(1,int(num/2) + 1):
                new_sol = dp[a] + dp[num - a]
                sol = min(sol, new_sol)
            dp[num] = sol
        return dp[-1]

class Solution:
    def numSquares(self, n: int) -> int:
        sr = int(sqrt(n))
        if sr*sr == n:
            return 1
        dp = [0]*(n + 1)
        dp[0] = 0
        for sr in range(1, sr + 1):
            dp[sr*sr] = 1
        for num in range(1, n + 1):
            if dp[num] == 0:
                sol = maxsize
                for a in range(1,int(num/2) + 1):
                    new_sol = dp[a] + dp[num - a]
                    sol = min(sol, new_sol)
                dp[num] = sol
        return dp[-1]        

# instead of partition any num into any two integers and check the dp, 
# we can partition the num into only a square number and num minus it.
# This way the search space is only O(sqrt(num)) for each num < n. A big
# saving as compared to O(num) in previous solutions.
# 
# Also, in the final solution, list is used to save squares. Initially ran
# into the problem of using set, and when iterating over squares, 
# if square > num then stop checking, but I forgot that set doesn't maintain
# the order. Hence, giving wrong result. Next time in test, use list 
# in preliminary attempts. Only use set when the last bits of performance 
# matters, or when improving the solutions.
class Solution:
    def numSquares(self, n: int) -> int:
        sr = int(sqrt(n))
        if sr*sr == n:
            return 1
        dp = [0]*(n + 1)
        dp[0] = 0
        squares = []
        for sr in range(1, sr + 1):
            squares.append(sr*sr)
        for num in range(1, n + 1):
            sol = dp[num - 1] + 1
            for sqr in squares:
                if sqr > num: break 
                new_sol = 1 + dp[num - sqr]
                sol = min(sol, new_sol)
            dp[num] = sol
        return dp[-1]

if __name__ == "__main__":
    print(Solution().numSquares(7691))