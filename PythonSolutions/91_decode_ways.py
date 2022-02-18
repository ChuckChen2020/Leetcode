#2021 May 15 22:45 - 23:54
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0]*(len(s) + 1)
        if s[0] == "0": return 0
        dp[0] = 1
        dp[1] = 1
        for i in range(2, len(s) + 1):
            if s[i - 1] == "0":
                if s[i - 2] == "0" or s[i-2] > "2":
                    return 0
                else:
                    dp[i] = dp[i - 2]
            else:
                if s[i - 2] == "0" or s[i-2:i] > "26":
                    dp[i] = dp[i-1]
                else:
                    dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]


if __name__ == "__main__":
    print(Solution().numDecodings("12307"))