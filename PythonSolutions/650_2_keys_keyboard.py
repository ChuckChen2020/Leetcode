# 2021 May 24, 13:18 - 14:10
from typing import List, Set, Tuple
from functools import lru_cache
class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1: return 0
        @lru_cache(maxsize=None)
        def dfs(num, cache, ops):
            if num == n:
                return ops
            if num > n:
                return float('inf')
            return min(dfs(num + cache, cache, ops + 1), dfs(2 * num, num, ops + 2))
        return dfs(2, 1, 2)

from math import sqrt
import sys

class Solution1:
    def minSteps(self, n: int) -> int:
        if n == 1: return 0
        dp = [-1 for _ in range(n+1)]
        dp[1] = 0
        for i in range(2, n + 1):
            dp[i] = i
            for j in range(2, i):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i // j)
        return dp[-1]


if __name__ == "__main__":
    #print(sys.getrecursionlimit())
    #sys.setrecursionlimit(3000)
    print(Solution1().minSteps(1000))