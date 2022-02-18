# 2021 June 13 10:04 - 10:37
from typing import List

# TLE O(n^2).
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n + 1):
            found = False
            for num in nums:
                if i ^ num == 0:
                    found = True
                    continue
            if not found: return i

# Using this 0^x == x, x^x == 0 idea, similar to Problem 136, if we start with a
# 0 and xor with 0-n and then xor with every element in nums. The final result
# will be the number that's been xor ed only once, that'd be the answer we
# wanted.

# What's invaluable about this idea, is that 0 xoring with two times a number, 
# the result gets back to zero. AND:

# xor operation is COMMUTATIVE. Meaning, a ^ b ^ c == a ^ c ^ b. So suppose a_i 
# is the one missing in a_1, ..., a_n:
#   0 ^ a_1 ^ ... ^ a_n ^ a_0 ^ ... ^ a_(i-1) ^ a_(i+1), ... ^ a_n 
# = 0 ^ a_1 ^ a_1 ^ a_2 ^ a_2 ^ ... ^ a_(i-1) ^ a_(i-1)^ a_i ^a_(i+1) ^ a_(i+1)^
# ... a_n ^ a_n 
# = a_i  

class Solution1:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n+1):
            ans ^= i
        for num in nums:
            ans ^= num

        return ans



if __name__ == "__main__":
    print(Solution().missingNumber([3,0,1]))
    print(Solution().missingNumber([0,1]))
    print(Solution().missingNumber([9,6,4,2,3,5,7,0,1]))
    print(Solution().missingNumber([0]))