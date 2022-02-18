# 2021 May 8 15:44 - 18:14 but finished quickly.
from typing import List, Set, Tuple
# Memory efficient yet slow. People must be using something else.
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(start, target, k, cur, ans):
            if k == 0:
                if target == 0:
                    # it's faster to make a copy here than in every dfs call.
                    #ans.append(cur)
                    ans.append(cur[:])
                return
            for i in range(start, 10):
                if i * k + (k - 1)*k/2 > target: return
                else:
                    cur.append(i)
                    #dfs(i+1, target - i, k - 1, cur[:], ans)
                    dfs(i+1, target - i, k - 1, cur, ans)
                    cur.pop()

        cur = []
        ans = []
        dfs(1, n, k, cur, ans)
        return ans


if __name__ == "__main__":
    print(Solution().combinationSum3(9,45))