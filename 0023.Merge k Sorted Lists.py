# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq as hp


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in range(len(lists)):
          if lists[i]:
            hp.heappush(heap, (lists[i].val, i))
            lists[i] = lists[i].next
        ans = ListNode()
        curr = ans

        while heap:
          val, node = hp.heappop(heap)
          curr.next = ListNode(val)
          curr = curr.next
          if lists[node]:
            hp.heappush(heap, (lists[node].val, node))
            lists[node] = lists[node].next

        return ans.next
