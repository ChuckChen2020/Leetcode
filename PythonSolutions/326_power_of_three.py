# 2021 June 3, 11:00 - 11:58
# The following way won't work. Errors can mess it up:
# >>> from math import log
# >>> log(243, 3)
# 4.999999999999999 round it to an int, in this case 5.
# Then, check pow(3, 5) == 243, so in fact it works!

from math import log
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        LOG3N = round(log(n,3))
        return pow(3, LOG3N) == n

# pow(3, int(log(pow(2,31), 3))) generates 1162261467, the largest pow of 3 in 
# the range of integer. If n is a pow of 3, 1162261467 mod n would be 0.
class Solution1:
    def isPowerOfThree(self, n: int) -> bool:
        return 1162261467 % n == 0 if n > 0 else False  

if __name__ == "__main__":
    print(Solution().isPowerOfThree(27))
    print(Solution().isPowerOfThree(-3))