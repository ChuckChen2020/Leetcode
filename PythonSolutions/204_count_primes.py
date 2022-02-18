# 2021 June 2, 17:14
# Recursion depth is a problem. Avoid using recursion could possibly make it work.
from math import sqrt
class Solution:
    def countPrimes(self, n: int) -> int:
        def isPrime(i):
            if i == n:
                return 0
            sr = int(sqrt(i))
            for fac in range(2, sr + 1):
                if i % fac == 0:
                    return isPrime(i+1)
            return 1 + isPrime(i+1)
        if n in (0,1): return 0
        return isPrime(2)

# TLE
class Solution1:
    def countPrimes(self, n: int) -> int:
        def isPrime(i):
            if i in (0,1): return 0
            sr = int(sqrt(i))
            for fac in range(sr, 1, -1):
                if i % fac == 0:
                    return 0
            return 1

        counter = 0
        for k in range(n):
            counter += isPrime(k)
        return counter

# Sieve of Eratos 6644 ms
class Solution2:
    def countPrimes(self, n: int) -> int:
        if n in (0,1,2): return 0
        cnt = 0
        non_primes = set()
        for i in range(2, n):
            if i in non_primes: continue
            num = (n - 1) // i
            # If the loop has come to i, non of the multiples of every number up # to i-1 doesn't include i, then i is indeed a prime. So we start with
            # 2 times of it.
            for k in range(2, num + 1):
                if k*i not in non_primes:
                    cnt += 1
                    non_primes.add(k*i)
        return n - 2 - cnt 

# Minor optimization on the range of multiples.
class Solution3:
    def countPrimes(self, n: int) -> int:
        if n in (0,1,2): return 0
        cnt = 0
        non_primes = set()
        for i in range(2, int(sqrt(n - 1)) + 1):
            if i in non_primes: continue
            num = (n - 1) // i
            for k in range(2, num + 1):
                if k*i not in non_primes:
                    cnt += 1
                    non_primes.add(k*i)
        return n - 2 - cnt 

# 1) Using array is somehow more space saving in practice. 
# 2) And a bit more squeezing on the second range of for loop. Any multiple of a 
# number less than or equal to i - 1 has already been considered, so instead of 
# 2, we can start with i. This means we start adding the non-primes from i^2.
# 1528ms, and 1/6 of memory used compared to the set approach. 
from math import sqrt
class Solution4:
    def countPrimes(self, n: int) -> int:
        if n in (0,1,2): return 0
        # 0, 1, 2, ..., n-1
        non_prime = [0]*n
        for i in range(2, int(sqrt(n - 1)) + 1):
            if non_prime[i] == 1: continue
            num = (n - 1) // i
            for k in range(i, num + 1):
                non_prime[k*i] = 1
        return n - 2 - sum(non_prime)

if __name__ == "__main__":
    from time import perf_counter
    t1 = perf_counter()
    print(Solution().countPrimes(5_000_000))
    print(perf_counter() - t1)