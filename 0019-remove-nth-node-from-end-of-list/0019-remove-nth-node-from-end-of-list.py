class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)  # Dummy node to handle edge cases
        fast = slow = dummy

        # Move fast n steps ahead
        for _ in range(n):
            fast = fast.next

        # Move fast to the end, maintaining the gap
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Skip the target node
        slow.next = slow.next.next

        return dummy.next
