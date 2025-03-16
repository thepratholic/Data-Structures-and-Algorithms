# Definiton of singly Linked List
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteNodeWithValueX(self, head, x):
        if head is None: return None

        if head.val == x:
            current = head
            head = head.next
            return head

        current = head
        while current.next:
            if current.next.val == x:
                current.next = current.next.next
                break
            current = current.next

        return head