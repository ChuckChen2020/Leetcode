# 2021 June 2 22:24 -22:35
class Solution:
    def convertToBase7(self, num: int) -> str:
        def divide_by_7(n):
            if n >= 0:
                return f"{n}" if n < 7 else divide_by_7(n // 7) + f"{n % 7}"
            else:
                return "-" + divide_by_7(-n)
        return divide_by_7(num)

if __name__ == "__main__":
    print(Solution().convertToBase7(100))
    print(Solution().convertToBase7(-7))