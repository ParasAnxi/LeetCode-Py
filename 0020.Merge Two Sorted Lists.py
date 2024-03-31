# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
      if not l1:
          return l2
      if not l2:
        return l1

      curr1 = l1
      curr2 = l2

      while curr1.next and curr2:
        if curr1.next.val >= curr2.val:
          next2 = curr2.next
          curr2.next = curr1.next
          curr1.next = curr2
          curr2 = next2
        else:
          curr1 = curr1.next

      if not curr1.next:
        curr1.next = curr2

      return l1

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      if not list1:
        return list2
      if not list2:
        return list1

      if list1.val < list2.val:
        return self.merge(list1, list2)
      else:
        return self.merge(list2, list1)
