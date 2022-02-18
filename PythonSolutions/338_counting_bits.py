# 2021 June 11, 13:28

# Recursive version gets TLE somehow, and might get recursion depth problem too.
# This is O(n) time complexity.
from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        for num in range(1, n + 1):
            count_num = ans[num // 2] + (num % 2)
            ans.append(count_num)
        return ans

# Or we get generate solutions from bottom-up: 
# 0: ['0'] -> [0]
# 1: ['0', '1'] -> [0, 1]
# 3: ['0', '1'] + ['10', '11'] in binary repr -> [0,1,1,2]
# 7: ['0','1','10','11','100', '101', '110', '111'] -> [0,1,1,2,1,2,2,3]
# ...
# O(logn) in time.
class Solution1:
    def countBits(self, n: int) -> List[int]:
        ans = [0,1]
        while n > len(ans) - 1:
            ans = ans + [x + 1 for x in ans]
        return ans[:(n + 1)] 


if __name__ == "__main__":
    print(Solution().countBits(0))
    print(Solution().countBits(1))
    print(Solution().countBits(2))
    print(Solution().countBits(5))
    print(Solution().countBits(85723))