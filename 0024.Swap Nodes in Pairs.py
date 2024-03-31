# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(-1)
        ans.next = head
        prev = ans
        while head and head.next:
          first = head
          second = head.next
          prev.next = second
          first.next = second.next
          second.next = first
          prev = first
          head = first.next
        return ans.next
