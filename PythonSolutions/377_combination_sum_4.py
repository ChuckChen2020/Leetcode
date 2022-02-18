# 2021 May 8 19:18 - 20:25 surrendered.
from typing import List, Set, Tuple
# TLE on [1,2,4], 32 it takes dynamic programming to solve the problem.
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def dfs(nums, target, cur, cnt):
            if target == 0:
                cnt[0] += 1
                return
            for i in range(len(nums)):
                if nums[i] > target: return
                cur.append(nums[i])
                dfs(nums, target - nums[i], cur, cnt)
                cur.pop()

        cur = []
        cnt = [0]
        nums.sort()
        dfs(nums, target, cur, cnt)
        return cnt[0]

# 3 ways to write the mutable counter.
def inc_counter(counter: int):
    # This one doesn't solve our problem.
    return counter + 1

# Pass a mutable object instead.
def inc_counter(counter: List[int]):
    counter[0] += 1

class counter(object):
    def __init__(self):
        self.counter = 0

    def increment(self):
        self.counter += 1
# Dynamic Programming: [1,2,3], 4
#       0 1 2 3
# dp = [1 ]
# t = 0: []
#     1: [1]
#     2: [2], [1,1]
#     3: [3], [1,2], [2,1], [1,1,1]
#     4: [1,3], [2,2], [1,1,2], [3,1], [1,2,1], [2,1,1], [1,1,1,1]
# For every t that is less than the real target, starting from initial value 0, dp[t] += dp[t-num] for every num in candidates that is less than t. Namely, appending num to each combination that sums to t - num would make one solution. The tallying has to be done on any num not greater than target.  
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0]*(target+1)
        dp[0] = 1
        for t in range(1, target + 1):
            for num in nums:
                if num <= t:
                    dp[t] += dp[t-num]
        return dp[-1]
            



if __name__ == "__main__":
    print(Solution().combinationSum4([1,2,3],4))