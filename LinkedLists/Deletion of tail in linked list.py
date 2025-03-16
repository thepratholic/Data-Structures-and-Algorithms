# Definiton of singly Linked List
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteTail(self, head):
        temp = head
        if head is None or head.next is None:
            return None

        while temp.next.next is not None:
            temp = temp.next
        temp.next = None
        return head