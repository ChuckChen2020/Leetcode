#2021 May 22, 17:39
from typing import List, Set, Tuple
# MLE
# class Solution:
#     def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
#         dp = [(0,0,0)]
#         for string in strs:
#             dp_cpy = dp[:]
#             x,y = string.count("0"), string.count("1")
#             for cnt, m0, n0 in dp_cpy:
#                 if m0 + x <= m and n0 + y <= n:
#                     dp.append((cnt + 1, m0 + x, n0 + y))
#         dp.sort()
#         return dp[-1][0]

# Filtering strategy might be entirely wrong!
# from copy import deepcopy
# class Solution:
#     def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
#         dp = [[] for _ in range(len(strs) + 1)]
#         dp[0].append([0,0])
#         for string in strs:
#             x,y = string.count("0"), string.count("1")
#             dp_cpy = deepcopy(dp)
#             for cnt, m_n_list in enumerate(dp):
#                 for m0, n0 in m_n_list:
#                     new_m, new_n = m0 + x, n0 + y
#                     if new_m <= m and new_n <=n:
#                         dp_cpy[cnt + 1].append([new_m, new_n])
        
#             for i in range(len(dp_cpy)):
#                 if len(dp_cpy[i]) == 0: continue
#                 mm, nn = min(map(lambda x: x[0], dp_cpy[i])), min(map(lambda x: x[1], dp_cpy[i]))
#                 if [mm, nn] in dp_cpy[i]:
#                     dp_cpy[i] = [[mm, nn]]
#                 else:
#                     mmm = min(map(lambda x: x[0],filter(lambda x: x[1] == nn, dp_cpy[i])))
#                     nnn = min(map(lambda x: x[1],filter(lambda x: x[0] == mm, dp_cpy[i])))
#                     dp_cpy[i] = [[mmm, nn], [mm, nnn]]
               
#             dp = dp_cpy

#         return dp
#         #return len(list(filter(lambda x: len(x) != 0, dp))) - 1

# 2d knapsack problem.
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0]*(m+1) for _ in range(n+1)]
        for s in strs:
            n_0, n_1 = s.count("0"), s.count("1")
            for row in range(n, n_1 - 1, -1):
                for col in range(m, n_0 - 1, -1):
                    dp[row][col] = max(dp[row][col], 1 + dp[row - n_1][col - n_0])

        return dp[-1][-1]




if __name__ == "__main__":
    #print(Solution().findMaxForm(["10","0001","111001","1","0"], 5,3))
    #print(Solution().findMaxForm(["10","0","1"], 2,2))
    #print(Solution().findMaxForm(["0","11","1000","01","0","101","1","1","1","0","0","0","0","1","0","0110101","0","11","01","00","01111","0011","1","1000","0","11101","1","0","10","0111"], 9, 80))
    print(Solution().findMaxForm(["0000111","0000111111","01111111","0001","000111111","0000001111111","00011111","000011111","00000011","0111111","0000000001111111","0011","001111","00000001111","0011","0000111111111","0001111111","011111111"],4,6))