# 2021 May 5, 10:20
from typing import List, Set, Tuple
# O(n^2), somehow only last 10%.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans_set = set()

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l not in [-1, len(nums)] and r not in [-1, len(nums)] and l < r:
                if nums[l] + nums[r] > - nums[i]:
                    right = nums[r]
                    while r not in [-1, len(nums)] and nums[r] == right:
                        r -= 1
                elif nums[l] + nums[r] < - nums[i]:
                    left = nums[l]
                    while l not in [-1, len(nums)] and nums[l] == left:
                        l += 1
                else:
                    ans_set.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1

        return [list(x) for x in ans_set]

# A more decent solution from Neetcode. The duplicate is removed through advancing i and adjusting l (then r adjuct automatically).
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]: continue
            l, r = i + 1, len(nums) - 1

            while l < r:
                if nums[l] + nums[r] > - nums[i]:
                    r -= 1
                elif nums[l] + nums[r] < - nums[i]:
                    l += 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1                    

        return ans

if __name__ == "__main__":
    print(Solution().threeSum([0,0]))