# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # Helper to get the kth node from current node
        def get_kth(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            kth = get_kth(group_prev, k)
            if not kth:
                break
            group_next = kth.next

            # Reverse the group
            prev = kth.next
            curr = group_prev.next

            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # Reconnect reversed group with previous part
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp

        return dummy.next
