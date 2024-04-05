# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        curr = head
        l = ListNode(0)
        c = l
        while curr:
          if curr.val < x:
            c.next = ListNode(curr.val)
            c = c.next
          curr = curr.next
        curr = head
        while curr:
          if curr.val >= x:
            c.next = ListNode(curr.val)
            c = c.next
          curr = curr.next
        return l.next
