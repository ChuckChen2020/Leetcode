# 2021 June 9 00:08

# O(n) time but not O(1) space.
from typing import List
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return counter.most_common()[-1][0]

# x ^ x = 0, x ^ 0 = x
# So for the elements that occur two times, after a round of xor, the result will
# revert back to 0, only for the one that appeared once, the result of the
# operations will be that number.
class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans

if __name__ == "__main__":
    print(Solution1().singleNumber([2,2,1]))
    print(Solution1().singleNumber([4,1,2,1,2]))
    print(Solution1().singleNumber([1]))