# 2021 June 14 09:56 - surrendered.

# Important Note:
# 1) constant space usually means modifies in place (input).
# 2) To mark that certain number has showed up, we can put a negative sign to
# the corresponding index. In this way, we note the existence of certain value
# without losing the values of each element.
# 3) In the end we only need to return the indices that still holds a positive
# value. So 2 passes should suffice.
from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            idx = abs(num) - 1
            nums[idx] = - nums[idx] if nums[idx] > 0 else nums[idx]
        ans = []
        for idx, num in enumerate(nums):
            if num > 0:
                ans.append(idx + 1)
        return ans

if __name__ == "__main__":
    print(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))
    print(Solution().findDisappearedNumbers([1,1]))