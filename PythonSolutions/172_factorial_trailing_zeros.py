# 2021 June 2 22:39 - gave up.

# It's pretty obvious that the number of trailing zeros is just the times of 10 
# the factorial n! has as factors. And it's also quite obvious that we can get 
# a lot more 2s than 5s. So the number of trailing zeros will be equal to
# the times n! has 5 as factors.

# Then I got stuck with what to do.
# 5! = 120
# 10! = ... 00
# 15! = ... 000
# 20! = ... 0000
# 25! = ... 000000, note that 25 brings in two more times of 5 instead of just 1!
# 30! = 7 times
# 35! = 8 times, etc.
# So, for n!, we have 1, 2, 3, ..., n as factors, in which,
# 5, 10, 15, 20, 25, 30, 35, ..., 5* (n // 5) are the ones that counts.
# But it's obvious that the above series contains numbers that have more than one
# 5 as a factor, like 25, 125, 625, ... What to do with them?
#
# if we divide the above series by 5, we get:
# 1, 2, 3, 4, 5, 6, ..., n // 5
# And n // 5 would be the number of 5s in the first round of division. Clearly,
# the above series still contains 5 and multiples of 5's and they're the ones
# like 25, 125, ... in the 0th round.
# 
# Now what to do is again pretty obvious, divide everything by 5 again!!!
# The number we get would be the additional 5s we get from numbers being 
# multiples of 25.
# 
# And it goes on and on.
# quot = sum = n // 5
# while quot != 0, quot = quot // 5, sum += quot
# In the end, sum will be the times of 5s.   
class Solution:
    def trailingZeroes(self, n: int) -> int:
        summation = 0
        while n != 0:
            n = n // 5
            summation += n
        return summation
        

if __name__ == "__main__":
    print(Solution().trailingZeroes(3))