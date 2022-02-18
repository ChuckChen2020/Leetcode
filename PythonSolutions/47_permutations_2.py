#2021 May 7 10:23-16:46
#Took a hell lot of time to get it right. NOTE: Inserting reps to rest is better than the other way around. As it's easier to find the index of last insertion. 
from typing import List, Set, Tuple 
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: return [[]]
        nums.sort()
        # if only identical elements left in the list, return. 
        if nums[0] == nums[-1]:
            return [nums]
        # else, fetch the largest identical elements. permute the rest.
        # for instance, nums = [1,2,3,3]
        last = nums.pop()
        reps = [last]
        while nums[-1] == last:
            reps.append(nums.pop())

        ans = self.permuteUnique(nums)
        # ans = [[1,2], [2,1]], reps = [3,3]
        # Now essentially for every per in ans, we have len(perm) + 1 slots to fill in all the identical elements.
        # We pop every one of them. and insert one each time.
        for _ in range(len(reps)):
            one_of_reps = reps.pop()
            # Now comes the tough part, managing the queue.
            # For every iteration, we pop a list in ans. Adding one element to it gives back multiple lists, so we make copies of list first and insert element at different positions, then return each of them to the right of the queue. Note: IT HAS TO BE A QUEUE. 
            for _ in range(len(ans)):
                perm = ans.pop(0)
                # One thing to take care of is the order, we only attach repetitive elements to the right of the last rep element. This avoids duplication in the ans.
                last_pos = len(perm) - 1
                while perm[last_pos] != one_of_reps:
                    last_pos -= 1
                    if last_pos == -1: break
                last_pos += 1
                # Last thing to notice is, we could possibly insert to the right of the entire list, which means i could end up being len(perm), hence the right bound in for.
                for i in range(last_pos, len(perm) + 1):
                    perm_cpy = perm[:]
                    perm_cpy.insert(i, one_of_reps)
                    ans.append(perm_cpy)
        return ans


if __name__ == "__main__":
    print(Solution().permuteUnique([1,1,2]))