#2021, April 24, 22:03 - 22:24
import math
def judgeSquareSum(c: int) -> bool:
        n = int(math.sqrt(c))
        squares = [pow(x,2) for x in range(n+1)]
        l = 0
        r = n
        while l <= r:
            square_sum = squares[l] + squares[r]
            if square_sum > c:
                r -= 1
            elif square_sum < c:
                l += 1
            else:
                return True
        return False
 

if __name__ == "__main__":
    print(judgeSquareSum(1))