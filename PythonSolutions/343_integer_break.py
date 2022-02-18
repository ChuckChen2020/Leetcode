# 2021 May 25 12:08 - 13:24
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1 for _ in range(0, n + 1)]
        for i in range(2, n + 1):
            for j in range(2, i):
                # dp[j] only include partitions of 2 or more factors that add up to j. Nonetheless, i can be partitioned into two factors j and i - j also. So (i-j)*j needs to be included.
                dp[i] = max(dp[i], dp[j]*(i-j), (i-j)*j)
        return dp[-1]

# It seems that the solution is 3^(n // 3) * 2 if n % 3 == 2.
# 3^(n // 3 - 1) * 4, if n % 3 == 1
# 3^(n // 3), if n % 3 == 0.
# with exceptions at n = 2, 3, 4
class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2: return 1
        if n == 3: return 2
        if n == 4: return 4
        mod = n % 3
        div = n // 3
        if mod in [0,1] and div >= 2:
            mod += 3
            div -= 1
        return pow(3, div)*mod



if __name__ == "__main__":
    print(Solution().integerBreak(36))