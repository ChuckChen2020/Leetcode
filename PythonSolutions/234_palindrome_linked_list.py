# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 2021 May 15, 14:28 - 14:57
from collections import deque
from typing import List, Set, Tuple
# This one breaks O(1) space complexity
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        queue = deque([])
        p = head
        while p != None:
            queue.append(p.val)
            p = p.next
        while len(queue) != 0:
            h = queue.popleft()
            if len(queue) != 0 and h != queue.pop():
                return False
        return True

# The brilliant idea from NeetCode.
# 1. Find middle, save the middle
# 2. Reverse the second half.
# 3. Have one pointer starting again from head, another from the old tail
#    compare the two pointers values until the left reaches the
#    middle (the middle, if odd number of nodes are given; or the right
#    middle in case even number of elements are given). 

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # Now slow points to the middle (or right middle).
        # Two pointers pl, pr are used for the shifting. It can't be done with just one pointer, as pl.next needs to point back to old pl, then some other pointer is needed to hold the next node.    
        pl = slow
        pr = slow.next
        mid = pl
        
        while pr:
            pl, pr, pl.next = pr, pr.next, pl
        p = head

        while p != mid:
            if p.val != pl.val: return False
            p = p.next
            pl = pl.next
        return True

# The second part modified in accordance with Leetcode problem 206.
# Note that setting prev, cur = None, slow automatically removes a loop
# inside the linklist, this becomes important in C++ solution.
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        prev, cur = None, slow
        
        while cur:
            prev, cur, prev.next = cur, cur.next, prev
        
        p = head

        while p != slow:
            if p.val != prev.val: return False
            p = p.next
            prev = prev.next
        return True