# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
            dummy = ListNode()  # Dummy node to start the merged list
            tail = dummy  # Pointer to track the last node in the merged list

            while list1 and list2:
                if list1.val < list2.val:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next
                tail = tail.next  # Move the tail pointer

            # Attach the remaining part of the non-empty list
            tail.next = list1 if list1 else list2

            return dummy.next 