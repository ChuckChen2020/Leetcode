# 2021 May 24 16:08- 17:50
from functools import lru_cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(maxsize=None)
        def dfs(i, j):
            if i == -1 and j == -1:
                return True
            if (i == -1 and j >= 0 and p[j] != "*") or (j == -1 and i >=0):
                return False
            if (i == -1 and j >= 0 and p[j] == "*"):
                return dfs(-1, j - 2)
            if p[j] == ".":
                return dfs(i - 1, j - 1)
            if p[j] == "*":
                if p[j-1] == ".":
                    for idx in range(i, -2, -1):
                        if dfs(idx, j-2): return True
                    return False
                else:
                    if p[j-1] == s[i]:
                        idx = i
                        while True:
                            if dfs(idx, j - 2): return True
                            if idx >= 0 and s[idx] == s[i]:
                                idx -= 1
                            else:
                                break
                        return False
                    else:
                        return dfs(i, j-2)
            if s[i] == p[j]:
                return dfs(i-1, j-1)
            else:
                return False
        return dfs(len(s) - 1, len(p) - 1)





                 

if __name__ == "__main__":
    print(Solution().isMatch("mississippi", "mis*is*p*."))
    print(Solution().isMatch("aab", "c*a*b"))
    print(Solution().isMatch("ab", ".*"))
    print(Solution().isMatch("aa", "a*"))
    print(Solution().isMatch("aa", "a"))