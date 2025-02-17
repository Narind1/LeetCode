class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)  # Use the provided ListNode class
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
        
        return dummy.next
