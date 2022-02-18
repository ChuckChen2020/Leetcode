# 2021 May 7, 19:05 - 19:52 surrendered.
# Huahua: c++ push_back是copy，所以你只要ans.append的时候copy就可以了，递归时不需要copy。
from typing import List, Set, Tuple
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, target, start, cur, ans):
            if target == 0:
                ans.append(cur)
                return
            for i in range(start, len(candidates)):
                num = candidates[i]
                # Pruning on the same level! If the first candidates is the same as the element before, it shouldn't be skipped. But any one after are on the same searching level, and should be skipped in case they're equal to the last to avoid duplicated answers.
                if i > start and num == candidates[i-1]: continue
                if num > target:
                    return
                else:
                    cur.append(num)
                    # Either pass a copy of cur here, or at ans.append().
                    # Otherwise the answer will be appended, then mutated back when the control flow is returned, at cur.pop(), ending up with a bunch of empty lists.
                    # C++ push_back is a copy, so it works like the following line.
                    dfs(candidates, target - num, i+1, cur[:], ans)
                    cur.pop() 

        candidates.sort()
        ans = []
        cur = []
        dfs(candidates, target, 0, cur, ans)
        return ans 

# Tackles the all one case much better.
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, target, start, cur, ans):
            if target == 0:
                ans.append(cur[:])
                return
            for i in range(start, len(candidates)):
                num = candidates[i]
                if i > start and num == candidates[i-1]: continue
                if num > target:
                    return
                else:
                    cur.append(num)
                    dfs(candidates, target - num, i+1, cur, ans)
                    cur.pop() 

        candidates.sort()
        ans = []
        cur = []
        dfs(candidates, target, 0, cur, ans)
        return ans

if __name__ == "__main__":
    print(Solution().combinationSum2([10,1,2,7,6,1,5], 8))

