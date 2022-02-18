# 2021 June 5 11:34 - 12:00
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(b) > len(a):
            return self.addBinary(b, a)
        carry = 0
        ans = ""
        for idx in range(-1, -len(a) - 1, -1):
            summation = int(a[idx]) + (int(b[idx]) if idx >= -len(b) else 0) + carry
            ans = str(summation % 2) + ans
            carry = summation // 2
        if carry: ans = "1" + ans
        return ans
             



if __name__ == "__main__":
    #print(Solution().addBinary("11", "1"))
    #print(Solution().addBinary("1010", "1011"))
    print(Solution().addBinary("1", "111"))