# 2021 June 8 21:31

# 1) Quite obviously, by doing xor, we get the bits where x and y differs.
# 2) n & (n - 1) flips the least significant 1 in n to 0, if we keep doing that
# till we reach n equals to all 0 in every bit (0), and count, we get the number
# of 1's.
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor_xy = x^y
        count = 0
        while xor_xy != 0:
            # Or just xor_xy &= xor_xy - 1
            xor_xy = xor_xy & (xor_xy - 1)
            count += 1
        return count

#The second part can also be tallied in the following way:
class Solution1:
    def hammingDistance(self, x: int, y: int) -> int:
        xor_xy = x^y
        count = 0
        while xor_xy != 0:
            count += xor_xy & 1
            xor_xy = xor_xy >> 1
        return count

if __name__ == "__main__":
    print(Solution1().hammingDistance(1,4))
    print(Solution1().hammingDistance(3,1))