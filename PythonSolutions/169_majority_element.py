# 2021 June 5 19:21

# Important Notes:
# Boyer-Moore majority vote algorithm
# Assume the first element to be the majority and count is set to 1,
# then go through the rest of the array, on each element:
# 1) if the element is the same as the majority, increment the count.
# 2) if the element is different than the majority, decrement the count.
# 3) if the count gets back to 0, it means there comes a draw between the
# "majority" and others, the majority is then switched to nums[i] and count 
# set to 1 again.
# 4) when the iteration hits the end, as long as the majority element exists,
# the majority should be it.
# The BM algorithm is a streaming algo, just like Reservoir sampling.  
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = nums[0]
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i] == majority:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0: 
                    majority = nums[i]
                    cnt = 1
        return majority

# The median must be the majority.
# Getting the median can be achieved at O(n). Median of medians algo.
from statistics import median
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return int(median(nums))

# Or ideas similar to Monte-Carlo type method can be used. Each time we randonly
# sample a number from the array. Going through the whole array to see if it is 
# indeed the majority. If not, just do it again. On average, 2 times of sampling 
# should be sufficient. And each time, testing the hypothesis takes O(n) ops.

if __name__ == "__main__":
    print(Solution().majorityElement([3,2,3]))
    print(Solution().majorityElement([2,2,1,1,1,2,2]))
    print(Solution().majorityElement([1,3,1,1,4,1,1,5,1,1,6,2,2]))