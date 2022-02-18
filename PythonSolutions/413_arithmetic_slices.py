# 2021 May 9 16:42 - 23:51
from typing import List, Set, Tuple
# The solution below turn out to include non-contiguous subsequences. So it's more advanced a search in a way.
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        def search(end):
            cnt = 0
            for i in range(1, end):
                diff = nums[end] - nums[i]
                j = i - 1
                while j >= 0:
                    if nums[i] - nums[j] > diff:
                        break
                    elif nums[i] - nums[j] < diff: 
                        j -= 1
                    else:
                        cnt += 1
                        i = j 
                        j = j - 1
            return cnt

        if len(nums) < 3:
            return 0
        dp = [0]*len(nums)
        for i in range(1, len(dp)):
            dp[i] = dp[i-1] + search(i)
        return dp[-1]  

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        def search(end):
            cnt = 0
            diff = nums[end] - nums[end - 1]
            for i in range(end - 1, 0, - 1):
                if nums[i] - nums[i-1] == diff:
                    cnt += 1
                else:
                    break
            return cnt

        if len(nums) < 3:
            return 0
        dp = [0]*len(nums)
        for i in range(1, len(dp)):
            dp[i] = dp[i-1] + search(i)
        return dp[-1]

if __name__ == "__main__":
    print(Solution().numberOfArithmeticSlices([1,2,3,4,5,6]))