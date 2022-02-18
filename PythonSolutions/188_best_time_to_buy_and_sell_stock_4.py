# 2021 May 12 11:46 - 13:46
from typing import List, Set, Tuple
from sys import maxsize
# At each day, you can possibly have 2k action/state:
# b1, s1, b2, s2, b3, s3, ... bk, sk
# with each state associated with the last state yesterday. e.g.,
# to sell for the first time, s1, at jth day, you have to find the b1
# of past days. And to achieve the highest book value, you have to use 
# the maximum book value of b1 at the past (which means at some day 
# <= j -1 you bought low and probably hold till jth), and add the price
# at jth day to it (sell it). It's the other way around for any buying 
# day.
# 
# tabular example: k = 3
# price     7   4   3   5   1   6   9   0   2   7
# b1        -7  -4  -3  -5  -1  -6  -9  0   -2  -7
# s1        /   -3  -1  2   -2  5   8   -1  2   7
# b2        /   /   -6  -6  1   -4  -4  8   6   1
# s2        /   /   /   -1  -5  7   10  1   10  15
# b3        /   /   /   /   0   -7  -2  10  8   3
# s3        /   /   /   /   /   6   9   0   12  17
# 
# When populating the table, you just check the row above for the
# max value before today. And add or subtract today's price accordingly.
# The maximum bv on the last day would be the answer.     
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        ROWS = 2*k
        bv = ['*' for _ in range(2*k)]
        bv[0] = - prices[0]
        for day in range(len(prices)):
            price_today = prices[day]
            for s in range(min(ROWS - 1, day), -1, -1):
                old_value = bv[s] if not isinstance(bv[s], str) else - maxsize - 1
                bv[s] = max((0 if s == 0 else bv[s-1]) + price_today * (1 if s % 2 == 1 else -1), old_value)
        return max(bv[:min(ROWS, len(prices))])

if __name__ == "__main__":
    print(Solution().maxProfit(2,[2,4,1]))