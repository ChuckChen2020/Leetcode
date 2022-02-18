# 2021 June 13 16:38

# Apparently, if we exclusive or every element, starting from 0, we get the xor
# of the two single elements.
# Then the question is, how do we find these two?
# The answer is:
#
# DIVIDE THEM INTO DIFFERENT GROUPS, USING BIT MASKS.
#
# For example, with [1,2,1,3,2,5], we xor from 0 and get 6. Where do we go from
# this? 
# 6 == (110)_2, and 
# 1) SET BITS OF XOR RESULTS INDICATE THAT THE TWO SINGLE NUMBERS HAVE 0 and 1 ON
# THAT BIT.
# So, we can, for instance, 
# 2) get the LSB of such xor result. (010)_2 in this case, to and mask all
# elements, the two singles can be seperated into different groups. All the two
# times elements should all fall into the same group and the xor would have no
# influence.
# 3) bitwise & should work.

from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_res = 0
        for num in nums:
            xor_res ^= num
        mask = xor_res & (- xor_res)
        single_1 = 0
        for num in nums:
            if num & mask == 0:
                single_1 ^= num
        return [single_1, single_1 ^ xor_res] 



if __name__ == "__main__":
    print(Solution().singleNumber([1,2,1,3,2,5]))
    print(Solution().singleNumber([-1,0]))
    print(Solution().singleNumber([0,1]))