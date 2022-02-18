# 2021 June 3 21:36 - 21:48
from typing import List
from random import shuffle
class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums
        self.nums = nums[:]
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.original[:]
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        shuffle(self.nums)
        return self.nums

# O(n^2), since pop is O(n)
from random import randrange, randint, random
def random_shuffle_1(nums):
    ret = []
    while len(nums) != 0:
        idx = randrange(0, len(nums))
        ret.append(nums.pop(idx))
    return ret

# O(nlogn)
from operator import itemgetter
def random_shuffle_2(nums):
    pairs = map(lambda x: [random(), x], nums)
    sorted_pairs = sorted(pairs)
    ans = map(lambda x: x[1], sorted_pairs)
    return list(ans)

# O(n) and modifies in place. Modern Fisher-Yates
def fisher_yates(nums):
    last_index = len(nums) - 1
    while last_index != 0:
        idx = randint(0, last_index)
        nums[idx], nums[last_index] = nums[last_index], nums[idx]
        last_index -= 1




# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

if __name__ == "__main__":
    from time import perf_counter
    nums = list(range(100))
    fisher_yates(nums)
    print(nums)

