#2021 May 16, 07:53 - 08:47
from typing import List, Set, Tuple
# Here the dp only holds the indices by which s[:index] is breakable into
# strings in wordDict. So when we march the index i, we just need to check 
# if s[an_index_in_dp: i] is in wordDict for all index in dp. Finally, if 
# len(s) is in dp, the whole string s would be breakable. 
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0]
        i = 1
        wds = set(wordDict)
        while i <= len(s):
            for brk in dp:
                if s[brk: i] in wds:
                    dp.append(i)
                    break
            i += 1
        return True if len(s) in dp else False




if __name__ == "__main__":
    print(Solution().wordBreak("leetcode", ["leet","code"]))