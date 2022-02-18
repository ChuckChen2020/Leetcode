# 2021 June 9 10:24

# The following way is simple enough.
from math import log
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and log(n, 4).is_integer()

# Coming from the more basic power of 2 problem, we have:
# 1) for any number that's qual to some power of 2, it's binary representation
# would be one set bit followed by all zeros. Thus, n-1 becomes, zero in the
# leading digit followed by all set bits. So it follows that n & (n-1) will be
# zero.
#
# However, here are the power of 4's in the binary format:
# >>> bin(4)
# '0b100'
# >>> bin(16)
# '0b10000'
# >>> bin(1)
# '0b1'
# >>> bin(64)
# '0b1000000'
# >>> bin(128)
# '0b10000000'
# So they are one set bit followed by EVEN number of zeros, making the set bit 
# always on odd bits. On the other hand, 
# >>> bin(8)
# '0b1000'
# The "power of 2 but not power of 4"s  will have their leading set bits on even # bits. So, if we combine the check 1) and:
# 2) n & (101010101...10)_2 == 0, then we know the only set bit will be on odd
# bit. With 2) we exclude the power of 2 but not 4 numbers.
# Now, to compute that filter,
# >>> num = "10"*16 (32 bits overall. The longest possible in the range given.)
# >>> int(num,2)
# 2863311530

# 28ms vs. 40+ms, quite a bit faster. 
class Solution1:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and not (n & (n-1)) and not (n & 2863311530)

if __name__ == "__main__":

    print(Solution().isPowerOfFour(16))
    print(Solution().isPowerOfFour(5))
    print(Solution().isPowerOfFour(1))