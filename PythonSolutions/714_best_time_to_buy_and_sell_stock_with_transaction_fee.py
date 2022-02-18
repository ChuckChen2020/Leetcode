# 2021 May 12 18:07 - 18:41
from typing import List, Set, Tuple
from sys import maxsize
# b, s, cw, cwo
# b = max(s_o, cwo_o) -fee - prices[day]
# s = max(b_o, cw_o) + price
# cw = max(b_o, cw_o)
# cwo = max(s_o, cwo_o)
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        b = - prices[0] - fee
        s = cw = '/'
        cwo = 0
        if len(prices) == 1: return 0
        for day in range(1, len(prices)):
            b_o, s_o, cw_o, cwo_o = (b,s,cw,cwo)
            cwo = max(-1 - maxsize if isinstance(s_o, str) else s_o, cwo_o)
            b = cwo - fee - prices[day]
            cw = max(b_o, -1 - maxsize if isinstance(cw_o, str) else cw_o)
            s = cw + prices[day]
        return max(b, cw, s, cwo)

if __name__ == "__main__":
    print(Solution().maxProfit([1,3,7,5,10,3], 3))