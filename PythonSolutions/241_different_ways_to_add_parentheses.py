# 2021 May 28, 12:23 -12:58 surrendered.
from typing import List
from functools import lru_cache
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def operation(sign, list1, list2):
            res = []
            for ele1 in list1:
                for ele2 in list2:
                    res.append(eval(str(ele1) + sign + str(ele2)))
            return res

        @lru_cache(maxsize=None)
        def ways(expr):
            if (expr.count('*'), expr.count('+'), expr.count('-')) == (0,0,0): 
                return [int(expr)]
            i = 0
            ans = []
            while True:
                while expr[i] not in ('+', '-', '*'):
                    i += 1
                    if i >= len(expr):
                        return ans
                expr1, sign, expr2 = expr[:i], expr[i], expr[i+1:]
                ans1, ans2 = ways(expr1), ways(expr2)
                ans.extend(operation(sign, ans1, ans2))
                i += 1
                
        return ways(expression)

# Some caller dispatch. This solution is a lot faster too!
# 44ms - 32ms.
from operator import add, sub, mul
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        operations = {
            '+': add,
            '-': sub,
            '*': mul
        }
        def operation(sign, list1, list2):
            res = []
            for ele1 in list1:
                for ele2 in list2:
                    res.append(operations[sign](ele1, ele2))
            return res
             
        @lru_cache(maxsize=None)
        def ways(expr):
            if (expr.count('*'), expr.count('+'), expr.count('-')) == (0,0,0): 
                return [int(expr)]
            i = 0
            ans = []
            while True:
                while expr[i] not in ('+', '-', '*'):
                    i += 1
                    if i >= len(expr):
                        return ans
                expr1, sign, expr2 = expr[:i], expr[i], expr[i+1:]
                ans1, ans2 = ways(expr1), ways(expr2)
                ans.extend(operation(sign, ans1, ans2))
                i += 1
                
        return ways(expression)

if __name__ == "__main__":
    print(Solution().diffWaysToCompute("2-1-1"))
    print(Solution().diffWaysToCompute("2*3-4*5"))
    print(Solution().diffWaysToCompute("11"))
    print(Solution().diffWaysToCompute("10+5"))