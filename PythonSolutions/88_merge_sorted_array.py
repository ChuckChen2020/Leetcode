# 2021， April 23, 14:54 - 15:35
from typing import List
def merge(nums1, m: int, nums2, n: int) -> None:
        index_1 = 0
        index_2 = 0
        nums1 = nums1[:m]
        queue = []

        while True:
            n1, n2 = nums1[index_1], nums2[index_2]
            if  n1 > n2:
                queue.append(n2)
                index_2 += 1
            else:
                queue.append(n1)
                index_1 += 1
            
            if index_1 == m:
                queue.extend(nums2[index_2:])
                break
            elif index_2 == n:
                queue.extend(nums1[index_1:])
                break            

        nums1 = queue

def merge_inplace(nums1, m: int, nums2, n: int) -> None:
        nums1[m:]= nums2
        nums1.sort()

# This is probably the desired way to do it.
def merge_1(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = q = 0
        while p <= m - 1 and q <= n - 1:
            if nums1[p] > nums2[q]:
                nums1[p+1:m+1] = nums1[p:m]
                nums1[p] = nums2[q]
                q += 1
                p += 1
                m += 1
            else:
                p += 1
        if p > m - 1:
            nums1[p:] = nums2[q:]

if __name__ == "__main__":
    merge_1([1,2,3,0,0,0], 3, [2,5,6], 3)