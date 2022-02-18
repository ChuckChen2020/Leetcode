# 2021 June 8 20:11 - 20:26
class Solution:
    def __init__(self):
        self.cache = set()
    def isHappy(self, n: int) -> bool:
        summation = 0
        while n > 0:
            summation += pow(n % 10, 2)
            n = n // 10
        if summation == 1: return True
        if summation in self.cache: return False
        self.cache.add(summation)
        return self.isHappy(summation)

if __name__ == "__main__":
    print(Solution().isHappy(19))
    print(Solution().isHappy(2))
