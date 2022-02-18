# 2021 June 8 23:38

# Create a number, whenever a bit is "torn down" from n, we add it to the number.
# So that in the end it represents the reverse of n.
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for _ in range(32):
            # left shift 1 bit
            ans = ans << 1
            # Add the last bit of n
            ans += n & 1
            # Get rid of the last bit of n.
            n = n >> 1
        return ans

# The binary integer can also be stored in the form of a string, and convert in
# one shot in the end. This is somehow faster.
class Solution1:
    def reverseBits(self, n: int) -> int:
        ans = ""
        for _ in range(32):
            ans += str(n & 1)
            # Get rid of the last bit of n.
            n = n >> 1
        return int(ans, 2)

if __name__ == "__main__":
    print(Solution1().reverseBits(0b00000010100101000001111010011100))
    print(Solution1().reverseBits(0b11111111111111111111111111111101))