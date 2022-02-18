# 2021 June 3 10:22 - 11:00
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def addRecursive(rev1, rev2):
            if len(rev1) < len(rev2):
                return addRecursive(rev2, rev1)
            ret = ""
            carry = 0
            for idx in range(len(rev1)):
                dig2 = 0 if idx >= len(rev2) else int(rev2[idx])
                sum_digs = int(rev1[idx]) + dig2 + carry
                if sum_digs >= 10:
                    # Attaching new digits to the left, so the order is already
                    # reversed in the returned string.
                    ret = str(sum_digs - 10) + ret
                    carry = 1
                else:
                    ret = str(sum_digs) + ret
                    carry = 0 
            # "1" + "9" = "10" instead of "0"
            if carry == 1: ret = "1" + ret
            return ret

        rev1, rev2 = num1[::-1], num2[::-1]
        ans = addRecursive(rev1, rev2)
        return ans
                    
             

if __name__ == "__main__":
    print(Solution().addStrings("11", "123"))
    print(Solution().addStrings("456", "77"))
    print(Solution().addStrings("0", "0"))
    print(Solution().addStrings("1", "9"))