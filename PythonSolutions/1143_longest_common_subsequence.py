# 2021 April 16. Surrendered entirely. 

# 2-d dp.
# text1 = "abcba", text2 = "abcbcba"
# At any two positions i, j in t1 and t2, if 1) t1[i] == t2[j]
# then the length of common subsequence count should increment by 1 and
# we then check from t1[i+1] and t2[j+1]. If 2) t1[i] != t2[j], then we 
# should keep on finding common susbequence of t1[i], t2[j+1] and t1[i+1]
# and t2[j], whichever includes a bigger common subsequence. So in the
# example, checking from the left to the right, "abcb" is common (logic 1)
# at work). Then we are left with "a" vs. "cba", "a","c" don't match, so
# dp of "a","c" refers to "","c" (0) and "a","b", which in turn refers
# to "", "b"(0) and "a", "a". Since "a","a" is a match, dp of it is 1 
# plus that of "", "", which is 0. So the boundary of common subseq 
# length all 0, propagates the value back to the topleft corner 
# dp[0][0] that we want, through some route that is determined by the
# matchings in the two texts. But algo won't know which route it takes
# beforehand, so solving the entire matrix, from bottom right to top left
# , would be necessary.      
#   dp  a   b   c   b   a   ""
#   a   1                   0
#   b       1               0
#   c           1           0
#   b               1       0
#   c                   *,1 0
#   b                   *,1 0
#   a                   1   0
#   ""  0   0   0   0   0   0
# * represents not knowing the value first, have to check right and
# downward. This checking keeps going until it reaches the bottom.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # One additional row and col to store bounary conditions.
        # 0, 1, ..., len(text1) - 1, for each char in text1, then len(text1) for boundary 0.
        ROWS, COLS = len(text1) + 1, len(text2) + 1 
        dp = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        for row in range(ROWS - 2, -1, -1):
            for col in range(COLS - 2, -1, -1):
                if text1[row] == text2[col]:
                    dp[row][col] = 1 + dp[row+1][col+1]
                else:
                    dp[row][col] = max(dp[row+1][col], dp[row][col+1])
        return dp[0][0]
            

            

if __name__ == "__main__":
    print(Solution().longestCommonSubsequence("papmretkborsrurgtina", "nsnupotstmnkfcfavaxgl"))