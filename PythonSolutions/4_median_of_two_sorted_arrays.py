# 2021 April 26, 17:41 - 19:16 surrendered.
from typing import List

# def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
#         if {len(nums1), len(nums2)} == {0,1}:
#             if len(nums1) != 0:
#                 return nums1[0]
#             else:
#                 return nums2[0]

#         l = 0
#         r = len(nums1) - 1
#         sum_len = len(nums1)+len(nums2)
#         while l <= r:
#             idx1 = int((l+r)/2)
#             idx2 = int((sum_len-1)/2) - idx1
#             if sum_len % 2 == 1:
#                 if nums2[idx2] > nums1[idx1]:
#                     l = idx1 + 1
#                 elif nums2[idx2 + 1] < nums1[idx1]:
#                     r = idx1 - 1
#                 else:
#                     return nums1[idx1]  

#             elif sum_len % 2 == 0:
#                 if nums2[idx2] > nums1[idx1] and (idx1 != len(nums1) - 1 or idx2 != 0):
#                     l = idx1 + 1
#                 elif nums2[idx2] < nums1[idx1] and (idx2 != len(nums2) - 1 or idx1 != 0):
#                     r = idx1 - 1
#                 else:
#                     return (nums1[idx1] + nums2[idx2])/2

# Observations on the problem:
# 1. if we perform search on the shorter list, the median might not appear in the list, so the l returned by binary search would be length of the list. However, in such case, the overall median should still be located at (half overall size - len(short array)). So regardless of whether the search hits back with valid indices, the candidates won't be missed, the validity of binary search approach is still guranteed (naturally caught) in this problem.
# 2. i, j are the seperation points at medians in nums1 and nums2 respectively. Meaning, [..... a[i],..., b[j]] corresponds to the [... left_median] in the gross sorted list, [.....a[i+1], ....b[j+1]] to [right_median, ......]. So left_median = max(a[i], b[j]), right_median = min(a[i+1], b[j+1]). 
import sys
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        sum_idx = int((len(nums1) + len(nums2) - 1)/2)
        # a[i+1], b[j], i+j+1 = sum_idx
        l = 0
        r = len(nums1) - 1

        while l <= r:
            idx1 = int((l+r)/2) # i+1
            idx2 = sum_idx - idx1 # j
            if nums1[idx1] < nums2[idx2]:
                l = idx1 + 1
            else:
                r = idx1 - 1

        idx1 = l # i+1
        idx2 = sum_idx - idx1 # j
        # max(a[i], b[j])
        left_median = max(-sys.maxsize-1 if idx1-1 < 0 else nums1[idx1-1], -sys.maxsize-1 if idx2 < 0 else nums2[idx2])


        if (len(nums1) + len(nums2)) % 2 == 1:
            return left_median
        # max(a[i+1], b[j+1])

        right_median = min(sys.maxsize if idx1 >= len(nums1) else nums1[idx1], sys.maxsize if idx2+1 >= len(nums2) else nums2[idx2+1])

        return (left_median + right_median)/2.0


if __name__ == "__main__":
    print(findMedianSortedArrays([1,2],[3,4]))