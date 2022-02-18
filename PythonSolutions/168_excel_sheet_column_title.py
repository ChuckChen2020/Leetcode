# 2021 June 5 10:13 - 10:59
# Intuitively, we need to do cN // 26, and take the remainder and see which char
# it corresponds to. However, there is an intricacy:
#
# cN % 26 gives us a number in [0, 25], what we want would be something in [1, 
# 26]. 
# 
# Notice here we should not simply add 1 to this [0, 25] result, as that
# effectively alters the mapping: for something that gives us 0 on the first
# digit, we should make it 26 and map it to "Z", instead of having it added by
# 1 and mapped to "A".
# 
# So the correct way to go about it, is to tear down a 26 from the quotient and
# make the remainder 26, in case when cN % 26 == 0. Now the quot. and rem get
# altered from (cN // 26, 0) to (cN // 26 - 1, 26).
# The rest is to offset the ascii value of "A" by 1, and break at a proper time.  
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while True:
            if columnNumber % 26 != 0:
                columnNumber, rem = columnNumber // 26, columnNumber % 26
            else:
                columnNumber, rem = columnNumber // 26 - 1, 26
            ans = chr(rem + ord("A") - 1) + ans
            if columnNumber < 1: break
        return ans

if __name__ == "__main__":
    print(Solution().convertToTitle(1))
    print(Solution().convertToTitle(28))
    print(Solution().convertToTitle(701))
    print(Solution().convertToTitle(2147483647))