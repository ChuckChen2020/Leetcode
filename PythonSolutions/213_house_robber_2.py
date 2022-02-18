# 2021 May 24, 19:10 -21:40
from typing import List, Set, Tuple
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2: return max(nums)
        dp_nh = [0]*len(nums)
        dp_h = [0]*len(nums)
        dp_h[1], dp_nh[1] = nums[0], nums[1]
        dp_h[2], dp_nh[2] = nums[0], max(nums[1], nums[2])
        for i in range(3, len(nums)):
            dp_h[i] = max(dp_h[i-2] + nums[i-1], dp_h[i-1])
            dp_nh[i] = max(dp_nh[i-2] + nums[i], dp_nh[i-1])
        return max(dp_h[-1], dp_nh[-1])


if __name__ == "__main__":
    print(Solution().rob([2,3,2]))
    print(Solution().rob([1,2,3,1]))
    print(Solution().rob([0]))
    print(Solution().rob([1,7,2,3,6,9,26,1]))
    print(Solution().rob([1,3]))
