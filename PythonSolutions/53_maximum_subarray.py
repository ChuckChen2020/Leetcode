#2021 May 25 10:26
from typing import List
# Find the accumulative sum at every index, the sum of any contiguous 
# subarray would be included in the difference of accumulative sums.
# So, we find the min and max of accumulative sum array to get the largest
# difference, provided that THE MINIMUM COMES BEFORE THE MAXIMUM. 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        acc = [0]*(len(nums) + 1)
        summation = 0
        for i in range(0, len(nums)):
            summation += nums[i]
            acc[i + 1] = summation
        m, max_df = acc[0], -float('inf')
        for i in range(1, len(acc)):
            max_df = max(max_df, acc[i] - m)
            if acc[i] < m: 
                m = acc[i]
        return max_df

# Pure dp way.
# Compute the maximum of accumulative sums of subarray up to the element,
# with the restriction that the current element must be included. 
# This means, max(sum + nums[i], nums[i]).
# The reason why we impose this restriction is that, when we look at the
# next element, we can be sure this sum we provide to it would contain at
# least the last element, which makes the result a sum of a contiguous 
# subarray.
  
class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = 0
        max_dp = -float('inf')
        for num in nums:
            dp = max(dp + num, num)
            max_dp = max(max_dp, dp)
        return max_dp


if __name__ == "__main__":
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(Solution().maxSubArray([1]))
    print(Solution().maxSubArray([5,4,-1,7,8]))
    print(Solution().maxSubArray([-1]))
    print(Solution().maxSubArray([-2,-1]))
    