# 2021 April 26, 15:18 - 15:40
from typing import List
def findMin(nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minimum = nums[-1]
        while l <= r:
            mid = int((l+r)/2)
            minimum = min(minimum, nums[l], nums[r], nums[mid])
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid - 1
            else:
                r -= 1
        return minimum


if __name__ == "__main__":
    print(findMin([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1]))