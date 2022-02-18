# 2021 April 28, 23:17
from typing import List
def findKthLargest(nums: List[int], k: int) -> int:
    nums = sorted(nums)
    return nums[-k]

# This is the quick select solution, supposedly O(n).
def findKthLargest_partition(nums: List[int], k: int) -> int:
        def partition(l: int, r: int) -> int:
            if l > r:
                return
            pivot = nums[r]
            p_index = l
            for i in range(l, r):
                if nums[i] < pivot:
                    nums[i], nums[p_index] = nums[p_index], nums[i]
                    p_index += 1
            nums[p_index], nums[r] = nums[r], nums[p_index]
            return p_index, r - p_index + 1

        l = 0
        r = len(nums) - 1
        while True:
            p_index, length = partition(l, r)
            if length > k:
                l = p_index + 1
            elif length < k:
                k -= length
                r = p_index - 1
            else:
                return nums[p_index]

# A more decent way to write the second part would be:
def findKthLargest_qs(nums: List[int], k: int) -> int:
        def quick_select(nums: List[int], l:int, r: int, k:int):
            def partition(nums: List[int], l: int, r: int) -> int:
                if l > r:
                    return
                pivot = nums[r]
                p_index = l
                for i in range(l, r):
                    if nums[i] < pivot:
                        nums[i], nums[p_index] = nums[p_index], nums[i]
                        p_index += 1
                nums[p_index], nums[r] = nums[r], nums[p_index]
                return p_index

            while l <= r:
                p_index = partition(nums, l, r)
                if p_index < len(nums) - k:
                    l = p_index + 1
                else:
                    r = p_index - 1
            return l
# The reason why the while loop in the second last function couldn't follow the pattern was because, the object of comparison, "length", was not the index itself. Always try to use the index and compare it with l and r. 

        index = quick_select(nums, 0, len(nums)-1, k)
        return nums[index]
            

            
        

# Heap solution, O(k*logn), also quite easy implementation wise if we use heapq.
import heapq
def findKthLargest_heap(nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return heapq.heappop(nums)


if __name__ == "__main__":
    print(findKthLargest_partition([1],1))
    print(findKthLargest_heap([3,2,3,1,2,4,5,5,6], 4))
    print(findKthLargest_qs([3,2,3,1,2,4,5,5,6], 4))