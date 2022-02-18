# 2021, April 25, 17:24 - 17:47
import time
def mySqrt(x: int) -> int:
        l = 0
        r = x
        while l <= r:
            mid = int((l + r) / 2)
            mid_sqr = pow(mid, 2)
            if mid_sqr > x:
                r = mid - 1
            elif mid_sqr == x or (mid_sqr < x and pow(mid + 1, 2)) > x:
                return mid
            else:
                l = mid + 1

def mySqrt_newton(x: int) -> int:
        a = x 
        while pow(a, 2) > x:
            a = int((a + x/a) / 2)
        return a 


if __name__ == "__main__":
    t1 = time.perf_counter()
    print(mySqrt(214739559957489512))
    print(time.perf_counter() - t1)
    t2 = time.perf_counter()
    print(mySqrt_newton(214739559957489512))
    print(time.perf_counter() - t2)