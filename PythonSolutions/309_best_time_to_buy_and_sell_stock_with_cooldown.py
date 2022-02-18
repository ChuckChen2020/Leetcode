# 2021 May 12 15:01 - 16:14
from typing import List, Set, Tuple
from sys import maxsize

# Actions/states at any day: buy, sell, cooldown with stock (possessing)
# and cooldown without.
# price     1   3   5   2   7
# b         -1  -3  -5  0   -3
# s         /   2   4   1   7
# c/w       /   -1  -1  -1  0
# c/wo      0   0   2   4   4
#
# Note that c/wo and c/w can't be merged into just cooldown, as c/wo can
# have a bookvalue greater than 0 (Bought and Sold and has made a fortune).
# 
# Any buy day could only be an immediate subsequent of c/wo (since
# multiple holds is not allowed). Sell come after either buy or c/w.
# c/w follows a buy or a c/w. c/wo follows either c/wo or a sell.
#
# b = cwo_o - price at the day
# s = max(b_o, cw_o) + price
# cw = max(b_o, cw_o)
# cwo = max(s_o, cwo_o)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b, s, cw, cwo = - prices[0], '/', '/', 0
        if len(prices) == 1: return 0
        for day in range(1, len(prices)):
            b_o, s_o, cw_o, cwo_o = (b,s,cw,cwo)
            b = cwo_o - prices[day]
            cw = max(b_o, - maxsize - 1 if isinstance(cw_o, str) else cw_o)
            s = cw + prices[day]
            cwo = max(- maxsize - 1 if isinstance(s_o, str) else s_o, cwo_o)
        return max(b,s,cw,cwo)

if __name__ == "__main__":
    print(Solution().maxProfit([1,3,5,2,7,9,5,4,6,3,2,9]))