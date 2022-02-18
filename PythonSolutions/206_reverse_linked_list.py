# 2021 May 15 17:50 - 18:04
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None: return head
        l = head
        r = head.next
        head.next = None
        while r:
            l, r, l.next = r, r.next, l
        return l

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, cur = None, head
        while cur:
            prev, cur, prev.next = cur, cur.next, prev
        return prev