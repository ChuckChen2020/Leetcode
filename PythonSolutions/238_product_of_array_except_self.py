# 2021 June 5 16:09 - surrendered.
# Important Notes:
# 1) Two passes, Forward and backward
# 2) The concept of prefix and postfix 
# prefix and postfix:
#           -1      1       0      -3       3
# prefix:   -1      -1      0       0       0
# postfix:   0      0       0      -9       3
# Then in order to get any requested product at index i,
# we need prefix[i-1]*postfix[i+1].
# 
# This method still uses O(n) space complexity,
# but we can use the output array, as hinted.
# Compute the prefix product and store them in the output array,
# Then we compute a postfix product and update it continuously after
# we compute the requested product. 
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        ans = []
        post = 1
        for num in nums:
            prefix *= num
            ans.append(prefix)
        for i in range(len(nums)-1, - 1, -1):
            ans[i] = (1 if i == 0 else ans[i-1])*post
            post *= nums[i]
        return ans


if __name__ == "__main__":
    print(Solution().productExceptSelf([1,2,3,4]))
    print(Solution().productExceptSelf([-1,1,0,-3,3]))