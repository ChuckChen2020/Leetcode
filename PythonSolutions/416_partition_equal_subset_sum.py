# 2021 May 21, 18:35
from typing import List, Set, Tuple
# The solution below ended up in TLE on a case with 200 elements.
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        half_sum = sum(nums) // 2
        dp = [set() for _ in range(half_sum + 1)]
        dp[0].add(tuple(0 for _ in range(len(nums))))
        for target in range(1, half_sum + 1):
            for idx, num in enumerate(nums):
                if num <= target:
                    for comb in dp[target - num]:
                        if comb[idx] == 0:
                            cpy = tuple(comb[i] if i != idx else 1 for i in range(len(nums)))
                            dp[target].add(cpy)
        return bool(len(dp[-1]))

#   dp starts with {0}.    
#   dp  
#   1       {0  1}
#   5       {0  1   5   6}
#   11      {0  1   5   6   11  12  16  17}
#   5       {0  1   5   6   11  12  16  17  10  21  22}
#   Each time we add in the addtional possible sum using the addional num
#   for each num in nums. And check if the target is in the dp.
#   This approach naturally avoided the need to tackle the possibility of 
#   duplicated use of any element BY TAKING ONLY THE SUM INSTEAD OF THE 
#   COMBINATIONS. Effectively equvalent to if we swap the two for outer
#   loop in the above solution, and the third for can then be avoided.  

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        half_sum = sum(nums) // 2
        dp = {0}
        for num in nums: #O(len(nums))
            dp_cpy = set()
            for ele in dp: #O(len(dp)) <= O(sum(nums))
                new = ele + num
                if new != half_sum:
                    dp_cpy.add(ele + num)
                else:
                    return True
            dp = dp.union(dp_cpy)
        return False

if __name__ == "__main__":
    print(Solution().canPartition([1,5,11,5]))
    #print(Solution().canPartition([100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,99,97]))