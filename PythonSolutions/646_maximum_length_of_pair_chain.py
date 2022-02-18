#2021 May 27 07:43 - 08:22
from typing import List, Set, Tuple
from functools import lru_cache
# 2788 ms
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        @lru_cache(maxsize=None)
        def dfs(i):
            max_chain = 1
            for j in range(i+1, len(pairs)):
                if pairs[j][0] > pairs[i][1]:
                    max_chain = max(max_chain, 1 + dfs(j))
            return max_chain
            
        max_len = 0
        for idx in range(len(pairs)):
            max_len = max(dfs(idx), max_len)
        return max_len

# Of course, to find the first pair in the sorted list that follows the current, 
# we can use binary search instead of going through everyone of them.
# 1600 ms.
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        @lru_cache(maxsize=None)
        def dfs(i):
            max_chain = 1
            l, r = i + 1, len(pairs) - 1
            while l <= r:
                m = (l + r) // 2
                if pairs[m][0] <= pairs[i][1]:
                    l = m + 1
                else:
                    r = m - 1
            for j in range(l, len(pairs)):
                max_chain = max(max_chain, 1 + dfs(j))                
            return max_chain
            
        max_len = 0
        for idx in range(len(pairs)):
            max_len = max(dfs(idx), max_len)
        return max_len

# From the back process to the front, if the pair doesn't follow any more, break from the for.
# This way even the the binary search can be avoided. 2084ms.
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        @lru_cache(maxsize=None)
        def dfs(i):
            max_chain = 1
            for j in range(len(pairs) - 1, i, -1):
                if pairs[j][0] <= pairs[i][1]: break
                max_chain = max(max_chain, 1 + dfs(j))                
            return max_chain
            
        max_len = 0
        for idx in range(len(pairs)):
            max_len = max(dfs(idx), max_len)
        return max_len

# dp is not as straightforward to come up with. It's not as much faster as I expected.
# For any pair that "follows" the current pair i, we might attach it to
# the current pair, and accrue the length of chain by 1. 
# The tally of pairs after the current all ties into the dp of i. 
# So the update needs to go from the back backwards.
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        dp = [1]*len(pairs)
        for i in range(len(dp) - 1, -1, -1):
            for j in range(len(dp) - 1, i, -1):
                if pairs[j][0] <= pairs[i][1]: break 
                dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)


if __name__ == "__main__":
    print(Solution().findLongestChain([[1,2],[2,3],[3,4]]))
    print(Solution().findLongestChain([[1,2],[7,8],[4,5]]))
    print(Solution().findLongestChain([[7,9],[4,5],[7,9],[-7,-1],[0,10],[3,10],[3,6],[2,3]]))