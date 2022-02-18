# 2021 May 30 18:55

# [3,1,5,8]
# Let's pop all elements in just one order 1, 5, 3, 8:
# sum:  0   +   3*1*5 =     15, [3,5,8] is left.
#       15  +   3*5*8 =     135 [3,8]   is left.
#       135 +   1*3*8 =     159 [8]     is left.
#       159 +   1*8*1 =     167 []      done.
 
# We popped 8 LAST in this case, which happens to be the max-yielding case. 1) But we might as well pop 3,1, or 5.
# 2) Looking at the first 3 steps, it's as if we're handling subsequence [3,1,5], with 8 being the imaginary
# right boundary. 
# Suppose f([3,1,5,8]) denotes a series of operation that maximize the outcome of popping. With the imaginary boundaries,
# nums = 1 [3 1 5 8] 1
# f(1 [3,1,5,8] 1) = max
#                (
#                       1*3*1 + f(3 [1,5,8] 1),
#                       f(1 [3] 1) + 1*1*1 + f(1 [5,8] 1),
#                       f(1 [3,1] 5) + 1*5*1 + f(5 [8] 1),
#                       f(1 [3,1,5] 8) + 1*8*1
#                )
# Note that: 1) the products of triplets all have 1 and 1 as bounaries, because we're popping those last. By then, none of
#               the adjacent elements would be present. Whereas, the popped element in the last round will be used as the
#               boundaries of their adjacent elements' popping.
#            2) We can see that to the eye of the function f, nums is as if never changed, only that when we feed in a subarray,
#               the imaginary boundaries could be the next/last element to the boundaries. 
# So, we formulate f into dp:
# dp[l][r] = max(dp[l][k-1] + nums[l-1]*nums[k]*nums[r+1] + dp[k+1][r]) | for l <= k <= r. 
# Top down memoization got TLE on 69th case.
from typing import List
from functools import lru_cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        N = len(nums)
        # 0, 1, ..., N, N+1
        nums = [1] + nums + [1]
        @lru_cache(maxsize=None)
        def dfs(l,r):
            if l > r:
                return 0
            max_val = 0
            for k in range(l, r+1):
                max_val = max(max_val, dfs(l,k - 1)+ nums[l-1]*nums[k]*nums[r+1]+ dfs(k+1,r))
            return max_val

        return dfs(1, N)
                


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        N = len(nums)
        #       0   1,...N, N+1
        nums = [1] + nums + [1]
        dp = [[0]*(N + 2) for _ in range(N + 2)]
        for length in range(1, N + 1):
            # r <= N -> l < N + 2 - length
            for l in range(1, N + 2 - length):
                r = l + length - 1
                for k in range(l, r + 1):
                    dp[l][r] = max(dp[l][r], dp[l][k-1] + nums[l-1]*nums[k]*nums[r+1] + dp[k+1][r])
        return dp

if __name__ == "__main__":
    print(Solution().maxCoins([1,5]))
    print(Solution().maxCoins([3,1,5,8]))