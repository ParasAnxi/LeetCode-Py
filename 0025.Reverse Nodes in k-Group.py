# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count, curr, prev, next = 0, head, None, None
        while curr and count < k:
          curr = curr.next
          count += 1
        if count == k:
          count = 0
          curr = head
          while curr and count < k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count += 1

          if next:
            head.next = self.reverseKGroup(next, k)
          return prev
        else:
          return head
