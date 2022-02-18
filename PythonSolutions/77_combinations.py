# 2021 May 3, 12:56 - 16:33
from typing import List
# a(n,k) = a(n-1, k) + a(n-1, k-1) in terms of number.
def combine(n: int, k: int) -> List[List[int]]:
        # base cases:
        if n == k:
            return [[x for x in range(1, n+1)]]
        if k == 0:
            return [[]]

        ans = combine(n-1, k)
        with_n = combine(n-1, k-1)

        for x in with_n:
            x.append(n)
        ans.extend(with_n)

        return ans
            

if __name__ == "__main__":
    print(combine(1,1))