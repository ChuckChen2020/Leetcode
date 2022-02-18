#2021 May 8, 13:45 - 14:21
from typing import List, Set, Tuple
# Very similar to 40. 
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, target, start, cur, ans):
            if target == 0 and cur not in ans:
                ans.append(cur)
                return
            for i in range(start, len(candidates)):
                num = candidates[i]
                if num > target: return
                else:
                    cur.append(num)
                    # starting index set to i, as the element can be reused.
                    # But we have sorted candidates to avoid repetitions.
                    # Also sorting makes it easier to identify duplications in ans.append.
                    dfs(candidates, target - num, i, cur[:], ans)
                    cur.pop()

        cur = []
        ans = []
        candidates.sort()
        dfs(candidates, target, 0, cur, ans)
        return ans


if __name__ == "__main__":
    print(Solution().combinationSum([1], 1))