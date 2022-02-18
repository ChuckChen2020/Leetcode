# 2021 June 5 17:17-17:51
from typing import List
from statistics import median
# Taking the derivatives of the summation of all distances,
# we can find that the it's equal to:
#                   sum of (x-xi)/abs(x-xi), i = 0, ..., len(nums) - 1
# when x != xi
# So it's either 1, or -1 in value. Naturally, if we keep half of them -1 and 
# the other half equals to 1, we'd get the derivative equal to 0. 
# The solution might not be unique, but median kinda achieves that. Roughly,
# half would be less and half would be greater.
#
# Note that with odd number of elements, median is straightforward. However, with # even number of elements, the median might not be an integer. Fortunately, in 
# such case, both the left floor of it or the ceiling of it would make half of 
# the elements less and half greater.
#
# Also notice that the mean value won't work. skewed values might drag the mean
# towards one end.
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        m = int(median(nums))
        steps = 0
        for num in nums:
            steps += abs(m - num)
        return steps


if __name__ == "__main__":
    print(Solution().minMoves2([1,2,3]))