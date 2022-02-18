#2021 May 12 10:55
from typing import List, Set, Tuple
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0]*len(prices)
        prev_low = prices[0]
        for i in range(1, len(prices)):
            dp[i] = max(dp[i-1], prices[i] - prev_low)
            prev_low = min(prev_low, prices[i])
        return dp[-1] 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = 0
        prev_low = prices[0]
        for price in prices:
            dp = max(dp, price - prev_low)
            prev_low = min(prev_low, price)
        return dp

if __name__ == "__main__":
    print(Solution1().maxProfit([7,1,5,3,6,4]))