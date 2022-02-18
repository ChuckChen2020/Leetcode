#2021 April 30, 14:15 - 14:33
from typing import List
def sortColors(nums: List[int]) -> None:
        def quick_sort(nums: List[int], l: int, r: int)->None:
            def partition(nums: List[int], l: int, r: int)->int:
                if l > r:
                    return
                pivot = nums[r]
                p_index = l
                for i in range(l,r):
                    if nums[i] < pivot:
                        nums[i], nums[p_index] = nums[p_index], nums[i]
                        p_index += 1
                nums[r], nums[p_index] = nums[p_index], nums[r]
                return p_index

            if l >= r:
                return
            p = partition(nums, l, r)
            quick_sort(nums, l, p - 1)
            quick_sort(nums, p + 1, r)

        quick_sort(nums, 0, len(nums) - 1)

# Quick_sort of course could solve the problem inplace. But since we already know the values would be [0,1,2]. This piece of info could greatly simply the solution: In only one traversal, if I see 0, put it to the left; if I see 2, put it to the right; 1, do nothing.
def sortColors_simple(nums: List[int]) -> None:
        r = len(nums)-1
        l = 0
        while l <= r:
            if nums[l] == 0:
                nums[0], nums[1:l+1] = 0, nums[0:l]
                l += 1
            elif nums[l] == 2:
                k = 0
                while nums[l+k] == 2:
                    k += 1
                    if l + k == len(nums):
                        return
                nums[-k:], nums[l:-k]= nums[l:l+k], nums[l+k:]
            else:
                l += 1 
 

if __name__ == "__main__":
    nums = [1]
    sortColors(nums)
    print(nums)
    nums = [1,2,0]
    sortColors_simple(nums)
    print(nums)
