# 2021 April 26, 16:01 - 16:45
from typing import List
def singleNonDuplicate(nums: List[int]) -> int:
        def odd_even(input:List[int])->List[int]:
            return [x % 2 for x in input]

        if len(nums) == 1:
            return nums[0]
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = int((l+r)/2)
            
            if (mid == 0 and nums[mid+1] != nums[mid]) or (mid == len(nums) - 1 and nums[mid-1] != nums[mid]) or mid not in (0, len(nums) - 1) and nums[mid-1] != nums[mid] and nums[mid+1] != nums[mid]:
                return nums[mid]
            else:
                m_i = [mid-1, mid] if nums[mid-1] == nums[mid] else [mid, mid+1]

                if odd_even([l, l+1]) == odd_even(m_i):
                    l = m_i[1] + 1
                else:
                    r = m_i[0] - 1


if __name__ == "__main__":
    print(singleNonDuplicate([1,1,2]))