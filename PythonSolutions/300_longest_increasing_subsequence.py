#2021 May 16 09:46 - 16:35 surrendered.
from typing import List, Set, Tuple
# Start with a case that wasted me: The number represent the length of
# longest possible subsequence starting from the index.
# The trick is really to go from backward to the beginning. 
#       4   10  4   3   8   9
#                           1
#                       2
#                   3
#               1
#           1
#       2
# Looking backward, the dp of last index is 1.
# On the second to the last, 8 < 9, so it's possible to have the 
# subsequence starting at the last index, and attach 8 to the beginning.
# so dp[-2] = max(1, 1 + dp[-1])
# Similarly, at any index i, for any j > i, if nums[j] > nums[i],
# we can update the dp[-i] = max(dp[-i], 1 + dp[-j]), which could
# potentially be repeated for all (n-i) indices. This makes the solution
# O(n^2). 
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        # Note that the first loop has to go from back to front.
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i+1, len(nums)):
                dp[i] = max(dp[i], 1 + dp[j] if nums[j] > nums[i] else 1)
        return max(dp)


# This O(nlogn) method is a magic!
# [4, 10, 4, 3, 8, 9]
# num   dp
# 4     [4]
# 10    [4,10]  \\ [4], [*,10]
# 4     [4,10] 
# 3     [3,10]  \\ [3], [*,10]
# 8     [3,8]   \\ [3], [*,8]
# 9     [3,8,9] \\ [3], [*,8], [*,*,9]
# It might seem like the dp is just holding the longest subsequece, but
# it's not! What the array is maintaining is the last element of the
# subsequnce of length 1, 2, ..., to maximum possible at the current index.
# And when it sees a new number, it can either 1) be used to extend one of 
# the shorter subsequences, and end up replacing the next length with a 
# smaller tail value of its, or 2) be the biggest of all tails in dp array 
# and thus extend the longest possible subsequence (it will end up
# appended to the end of dp array), or 3) if it's smaller than any element
# in the dp array, nothing should be done about it.
# 
# Now comes the best part of this method: The dp array is IN ASCENDING ORDER
# and BINARY SEARCH CAN BE USED TO FIND THE POSITION OF NEW ELEMENT AND
# DETERMINE WHAT TO DO WITH IT THEREBY. This is what makes the method 
# O(nlogn).

from bisect import bisect_left
class Solution1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        dp.append([nums[0]])
        for i in range(1, len(nums)):
            number = nums[i]
            dp.append(dp[-1][:])
            pos = bisect_left(dp[i], number)
            if pos == len(dp[i]):
                dp[i].append(number)
            elif pos < len(dp[i]) and pos >= 0:
                dp[i][pos] = number
        return len(dp[-1])
         
# Don't have to maintain the dp for each index. I'm totally beaten here.
class Solution1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for x in nums:
            pos = bisect_left(dp, x)
            if pos == len(dp):
                dp.append(x)
            else:
                dp[pos] = x
        return len(dp)

if __name__ == "__main__":
    print(Solution1().lengthOfLIS([7,7,7,7,7,7,7]))