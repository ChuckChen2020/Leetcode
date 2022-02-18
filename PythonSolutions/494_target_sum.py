#2021 May 27 14:21 - 14:36
from typing import List, Set, Tuple
from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(maxsize=None)
        def dfs(i, t):
            if i == len(nums) and t == 0:
                return 1
            if i == len(nums) and t != 0:
                return 0
            return dfs(i + 1, t + nums[i]) + dfs(i + 1, t - nums[i])
        return dfs(0, target) 

# dp solution
# Note that the special case of nums[0] == 0 would cause dp = Counter({nums[0]: 1, - nums[0]: 1})
# to initialize two key value pairs for [0,1], which is not correct. 
# An if condition to branch that out would be needed.
# List is easier to implement, but dictionary or Counter feels more feasible for this case.
from collections import Counter
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if nums[0] != 0:
            dp = Counter({nums[0]: 1, - nums[0]: 1})
        else:
            dp = Counter({nums[0]: 2})
        dp_new = Counter()
        for i in range(1, len(nums)):
            dp_new.clear()
            for key, value in dp.items():
                new_1, new_2 = key + nums[i], key - nums[i]
                dp_new[new_1] += value
                dp_new[new_2] += value
            dp = Counter(dp_new)
        return dp[target]


if __name__ == "__main__":
    print(Solution().findTargetSumWays([1,1,1,1,1], 3))
    print(Solution().findTargetSumWays([1], 1))
    print(Solution().findTargetSumWays([1,2,3,4,5,6,7,8,9,10], 7))
    print(Solution().findTargetSumWays([0,0,0,0,0,0,0,0,1], 1))