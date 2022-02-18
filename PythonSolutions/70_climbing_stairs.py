# 2021 May 9 16:11
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        # index 0 to n-1 corresponds to steps = 1 to n.
        dp = [0]*n
        dp[0] = 1
        dp[1] = 2
        for t in range(2,n):
            dp[t] = dp[t-1] + dp[t-2]
        return dp[-1]

if __name__ == "__main__":
    print(Solution().climbStairs(3))