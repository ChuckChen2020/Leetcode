# 2021 June 13 13:48 - 14:06

# 10101 
# 01010
# Naturally, the sum would be 11111, which is 100000 - 1.
# The essence then is to know the length of its bits representation.

class Solution:
    def findComplement(self, num: int) -> int:
        cnt = 0
        orig = num
        while num != 0:
            num >>= 1
            cnt += 1
        return (1 << cnt) - 1 - orig

# Or else, we can certainly flip it bit-by-bit. Speed-wise quite comparable to
# the last solution. Since there's no 
class Solution1:
    def findComplement(self, num: int) -> int:
        ans = 0
        bit = 0
        while num != 0:
            ans += ((num & 1) ^ 1) << bit
            bit += 1
            num >>= 1
        return ans

# Now comes the most efficient solution to this problem!
# A trick to get the most significant bit:
# for any n,
# n |= n >> 1
# n |= n >> 2
# n |= n >> 4
# n |= n >> 8
# n |= n >> 16
# Started with a 32 bit int n, it's guranteed that we'd get all 1's with the same
# number of bits, after the above operations. And this is because:
# 1) The most significant bit (left bit) would always be a set bit.
# 2) Oring n and n >> 1 would give us n WITH 2 LEADING SET BITS.
# 3) Now when we bitwise or n with n >> 2, we get n with 4 set bits, and it keeps
# going.
# 4) Since we get at most 32 set bits in 32 bit int, the above 5 ops would
# gurantee that n would be all set by the end.
# 5) If we don't get to certain shifts, but already has an all-set n, then what 
# the following operations do would be only oring n with 0, making the result
# stays at n.
# With this idea, we can solve it as follow:

class Solution2:
    def findComplement(self, num: int) -> int:
        orig = num
        num |= num >> 1
        num |= num >> 2
        num |= num >> 4
        num |= num >> 8
        num |= num >> 16
        return num - orig

if __name__ == "__main__":
    print(Solution2().findComplement(5))
    print(Solution2().findComplement(1))