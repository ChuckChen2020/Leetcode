# 2021 June 13 10:57

# xor with "10101 ... 01" and "1010 ... 10", one of the result should be 1111 ...1
# bitwise not it, it should then be 0.
#
# >>> a = "10"*16
# >>> a
# '10101010101010101010101010101010'
# >>> int(a, 2)
# 2863311530
# >>> a = "01"*16
# >>> int(a, 2)
# 1431655765
# This way won't work, as there are alternating 1 and 0's left on the significant
# bits. 

# O(n) solution can be achieved as follow:

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        last_bit = n & 1
        while n != 0 and n & 1 == last_bit:
            last_bit = (last_bit + 1) % 2
            n >>= 1
        return True if n == 0 else False

# A smarter way to toggle 0,1 is to use XOR:
# last_bit ^= 1        
class Solution1:
    def hasAlternatingBits(self, n: int) -> bool:
        last_bit = n & 1
        while n != 0 and n & 1 == last_bit:
            last_bit ^= 1
            n >>= 1
        return True if n == 0 else False            

if __name__ == "__main__":
    print(Solution().hasAlternatingBits(5))
    print(Solution().hasAlternatingBits(7))
    print(Solution().hasAlternatingBits(11))
    print(Solution().hasAlternatingBits(10))
    print(Solution().hasAlternatingBits(3))