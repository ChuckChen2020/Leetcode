# 2021 June 4 12:00 - 13:49
# The second solution took a bit time to come up with.
from typing import List
from random import choices
class Solution:
    def __init__(self, w: List[int]):
        self.weights = w

    def pickIndex(self) -> int:
        # [0] because the choices function returns a list, considering k can be 
        # more than 1.
        return choices(range(len(self.weights)), weights=self.weights, k=1)[0]
        
# The most brutal force way would be to add an index multiple times to a sample
# space according to weight distribution. The certainly works but could hit limit
# on time and space complexity.
# TLE
from random import choice
class Solution:

    def __init__(self, w: List[int]):
        sample_space = []
        for idx, weight in enumerate(w):
            for _ in range(weight):
                sample_space.append(idx)
        self.sample_space = sample_space

    def pickIndex(self) -> int:
        return choice(self.sample_space)

# The following solution is an improved version of the above idea.
# 1) Instead of appending elements directly into a list, we create an accumulated
# weight list which basically holds the CDF of the indices.
# 2) Randomly generate a number in range between [0, rightmost element in CDF)
# 3) Find where the random number falls, this can be done using binary search.
# 
# What's worth mentioning is the difference between bisect_left and bisect_right.
# In this problem the difference really matters.
# bisect_left returns the leftmost position to insert the element. And the other
# way round for bisect_right.
# So, for instance, we have [1,2,3,4,5,5,5,6,7,8]
# bisect_left will put 5 after 4. bisect_right will put 5 before 6.
# In our use case, we have a CDF, for instance, 
# [0, 3, 17, 18, 25]
# We want   [0,3)   [3,17)  [17, 18)    [18,25)
#           0       1       2           3
# So if we pick bisect_left, at randome sample = 3, the index is gonna 
# go left to the last index 0, while (3,17) goes to 1. This is hard to deal with.
# Using bisect_right, on, e.g., [3,17), the index points to 2. We can offset by
# 1 index left.
#
# Also, in random sampling, we won't want 25. Because bisect_right is gonna 
# bring the index to the one next to that of 25 (which doesn't exist already), 
# and then it's subtracted by 1, bring it back to the index corresponding to 25,
# which is, still, not included.
# So we want [0, 25) in random sampling. randrange does it better than randint.  
from bisect import bisect_right
from random import randrange
class Solution:

    def __init__(self, w: List[int]):
        acc = 0
        acc_list = []
        self.indices = range(len(w))
        for weight in w:
            acc_list.append(acc)
            acc += weight
        acc_list.append(acc)
        self.acc_list = acc_list

    def pickIndex(self) -> int:
        rnd = randrange(0, self.acc_list[-1])
        rnd_idx = bisect_right(self.acc_list, rnd) - 1
        return self.indices[rnd_idx]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()