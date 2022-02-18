# 2021 May 23 16:25 - 17:07
from typing import List, Set, Tuple
from collections import deque
from time import perf_counter
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        dp = [0]
        num = 1
        while True:
            dp_set = set(dp)
            for _ in range(len(dp)):
                val = dp.pop(0)
                for coin in coins:
                    new_val = val + coin
                    if new_val == amount:
                        return num
                    else:
                        if new_val not in dp_set:
                            dp.append(new_val)
                            dp_set.add(new_val)
            dp.sort()
            dp_set.clear()
            if dp[0] > amount: return -1
            num += 1

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        dp = deque([0])
        num = 1
        while True:
            dp_set = set(dp)
            for _ in range(len(dp)):
                val = dp.popleft()
                for coin in coins:
                    new_val = val + coin
                    if new_val == amount:
                        return num
                    elif new_val < amount and new_val not in dp_set:
                        dp.append(new_val)
                        dp_set.add(new_val)
            dp_set.clear()
            if len(dp) == 0: return -1
            num += 1

if __name__ == "__main__":
    t = perf_counter()
    print(Solution().coinChange([2,4,6,8,10,12,14,16,18,20,22,24], 9999))
    print(perf_counter() - t)