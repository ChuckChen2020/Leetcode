#2021, April 23, 16:58-17:34
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        p_slow = head
        p_fast = head
        p_vangard = head
        while True:
            p_slow = p_slow.next
            if p_fast is not None and p_fast.next is not None:
                p_fast = p_fast.next.next
            else:
                return None
            p_vangard = p_vangard.next
            
            if p_fast == p_slow:
                break
        p = head
        while True:
            if (p == p_vangard):
                return p
            p = p.next
            p_vangard = p_vangard.next