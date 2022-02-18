#2021 May, 2, 14:49 - 15:16
from typing import List 
from functools import lru_cache
def permute(nums: List[int]) -> List[List[int]]:
        @lru_cache(maxsize=None)
        def recursion(i: int):
            if i == 0:
                return [nums[0:1]]

            last_list = recursion(i - 1)
            ret = []
            for x in last_list:
                for k in range(0, len(x) + 1):
                    new_list = x[:]
                    new_list.insert(k, nums[i])
                    ret.append(new_list)
            return ret

        for i in range(0, len(nums)-1):
            recursion(i)        

        return recursion(len(nums) - 1)

def permute_recursion(nums: List[int]) -> List[List[int]]:
        ans = []
        # base case
        if len(nums) == 1:
            return [nums[:]]
        # Suppose we look at all permutations of length n. Taking away the last element, which can be any one of nums[0:len(nums)], we should be looking at all permutations of the other len(nums) - 1 elements. 
        for i in range(len(nums)):
            last = nums.pop(i)
            # permutation of the remaining len(nums) - 1.
            perms = permute_recursion(nums)
            # Add back the last one and push them to the ans.
            for x in perms:
                x.append(last)
            ans.extend(perms)
            #ans.extend([x.append(last) for x in perms])
            # Don't forget to add the element back to nums, so that the next iter plocks another element away from the original nums.
            nums.insert(i, last)
        return ans

if __name__  == "__main__":
    print(permute([1]))
    print(permute_recursion([1,2,3]))
        