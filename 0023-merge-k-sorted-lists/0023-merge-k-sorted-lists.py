import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        heap = []
        count = 0  # tie-breaker for nodes with equal value

        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, count, l))
                count += 1

        dummy = ListNode(0)
        curr = dummy

        while heap:
            val, _, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, count, node.next))
                count += 1

        return dummy.next
