#2021 April 26, 11:43 - surrendered on 13:00
# The solution below took me a hell lot of time and failed pathetically on the almost-all-1 cases. Now accepted.
from typing import List
def search(nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return False
        if len(nums) == 1:
            return target == nums[0]
            
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = int((l+r)/2)
            if target in (nums[l], nums[mid], nums[r]):
                return True

            if nums[r] < nums[mid]:
                if target > nums[mid] or target < nums[r]:
                    l = mid + 1
                elif target > nums[r] and target < nums[mid]:
                    r = mid - 1
            elif nums[r] > nums[mid]:
                if target > nums[r] or target < nums[mid]:
                    r = mid - 1
                elif target > nums[mid] and target < nums[r]:
                    l = mid + 1
            else:
                r -= 1
            
        return False

    

if __name__ == "__main__":
    print(search([1,1], 1))