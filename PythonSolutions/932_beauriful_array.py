# 2021 May 29 16:30 -17:05
from typing import List
import random
# TLE
# Initially tried to return just one solution for each n - 1, but when it comes to n,
# not all solution of n-1 allows for an insertion of n that doesn't create conflicts.
# So we computed all the viable solutions for each n - 1. And generate solution of n
# based on any n-1 solution possible. But TLE is there even at n == 37.
class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        def allBeautifulArrays(n):
            if n == 1: return [1]
            if n == 2: return [[1,2], [2,1]]
            ans = []
            prev_perms = allBeautifulArrays(n - 1)
            for prev in prev_perms:
                indices = [0]*(len(prev) + 1)
                for idx, x in enumerate(prev):
                    indices[x] = idx
                min_mid = n // 2 + 1
                greater_than, less_than = 0, n - 1
                for mid in range(n - 1, min_mid - 1, -1):
                    lesser = 2*mid - n
                    idx_mid, idx_lesser = indices[mid], indices[lesser]
                    if idx_mid > idx_lesser:
                        less_than = min(less_than, idx_mid)
                    else:
                        greater_than = max(greater_than, idx_mid + 1)

                if greater_than <= less_than:
                    for pos in range(greater_than, less_than + 1):
                        tmp = prev[:]
                        tmp.insert(pos, n)
                        ans.append(tmp)
            return ans

        return random.choice(allBeautifulArrays(n)) 

# The idea behind this solution is divide and conquer
# Spliting the domain into two. But not just spliting by median: [1,2,...n//2], [n//2, ..., n].
# 1) odds + even!
# Because for any i < j, and k in range (i,j), where 2*a[k] = a[i] + a[j], which we wanna break.
# if we pick a[i] to be odd, and a[j] to be even, then there will be no such a[k].
# So, if we keep first half of the array all odd, second half all even (or vice versa), 
# Then there won't be any corss-half a[i], a[j]'s, for which we can find a[k].
#
# 2) What about the halves themselves? How do we keep them "beautiful"? 
# We can generate them by mapping from a beautiful array:
# With [1,3,2] as a beutiful array, we can make:
# [1,5,3], which is 2*[1,3,2] - 1, and [2,6,4], which is 2*[1,3,2].
# And [1,5,3,2,6,4] would be beautiful, due to point 1).  

from functools import lru_cache
class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        @lru_cache(maxsize=None)
        def helper(N):
            if N == 1:
                return [1]
            odds_base = helper(N // 2 + N % 2)
            evens_base = helper(N // 2)
            return [2*x - 1 for x in odds_base] + [2*x for x in evens_base]
        return helper(n)



if __name__ == "__main__":
    print(Solution().beautifulArray(100))