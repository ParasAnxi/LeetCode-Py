# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
      if not head or not head.next or k == 0:
        return head

      tail = head
      size = 1

      while tail.next:
        size += 1
        tail = tail.next

      tail.next = head
      k = k % size

      last = size - k
      temp = head

      while last > 1:
        temp = temp.next
        last -= 1

      head = temp.next
      temp.next = None

      return head
