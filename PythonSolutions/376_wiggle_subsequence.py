# 2021 May 27, 11:13 - 11:47
from typing import List, Set, Tuple
from functools import lru_cache

# There must be a ton of optimization to do.
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dfs(i, factor):
            longest = 1
            for j in range(i+1, len(nums)):
                if factor*(nums[j] - nums[i]) > 0:
                    longest = max(longest, 1 + dfs(j, - factor))
            return longest

        max_len = 0
        for k in range(len(nums)):
            max_len = max(max_len, dfs(k, 1), dfs(k, -1))
        return max_len

# dp solution? 
# It feels pretty natural to maintain two rows dp table where one maintains 
# a sequence that starts with and increase and the other one maintains the
# length of a seq that starts with a decrease.

# 28 ms vs 292 ms in the brute force solution!

# Initially thought of maintaining [[t1, c1],[t2, c2]] as any element in dp, where t1, t2 denotes
# the tails of the two sequences (one starts with +, one with -), and c1, c2 denotes the counts of
# the length. But found out that in order to achieve the optimum length of the two, TAILS OF THEM 
# BOTH SHOULD BE JUST THE PREVIOUS ELEMENT in nums, and here's why:

# Suppose we need a nums[i] that is greater than the tail, and 
# 1) nums[i] > tail, we can simply increment the length for this sequence by 1 and toggle the factor 
#   (expect the reversed relation in the next round). And the new tail would actually be nums[i].
# 2) nums[i] <= tail, we can actually still set the new tail to be nums[i], s.t. it becomes easier
#   for the next element to be gt the tail. Only that we don't increment the length, nor do we toggle
#   the sign, as the length did not find nums[i] to have the expected relation with the old tail, and
#   we want the same relation in the next round.
# 
# This effectively collapse the recorded data to only [c1, c2] for each element in nums. Hence the 
# following implementation:   

class Solution1:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        dp = [[1,1]]
        factor_1, factor_2 = 1, -1
        for i in range(1, len(nums)):
            cnt_1, cnt_2 = dp[-1][:]
            if (nums[i] - nums[i-1])*factor_1 > 0:
                cnt_1 += 1                
                factor_1 *= -1
            if (nums[i] - nums[i-1])*factor_2 > 0:
                cnt_2 += 1
                factor_2 *= -1
            dp.append([cnt_1, cnt_2])
        return max(dp[-1])

# Note that we still have to maintain two seperated factors, as they MIGHT NOT ALWAYS HAVE 
# OPPOSITE SIGNS. For instance, in the [1,7,4,9,2,5] case, at i = 1, the first seq 
# effectively becomes [1,7], while the second becomes [7]. At this time, we'd want the next
# element to be less than the tails in both sequence. 

# In this dp solution, t is the observation on the optimum way to maintain the sequence, 
# especially when the next element doesn't have the expected relation with the current that 
# saves the cost in time or space (memoization) as compared to the brute force solution.
            
            

if __name__ == "__main__":
    print(Solution().wiggleMaxLength([1,7,4,9,2,5]))
    print(Solution().wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))
    print(Solution().wiggleMaxLength([1,2,3,4,5,6,7,8,9]))
    print(Solution().wiggleMaxLength([1,5,2,4,3,7,6,9,8,7,3,4,1,5,10,3,18]))