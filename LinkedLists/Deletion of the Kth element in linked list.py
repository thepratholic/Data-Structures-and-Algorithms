# Definiton of singly Linked List
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteKthNode(self, head, k):
        if head is None:
            return None
        if k == 1:
            current = head
            head = head.next
            return head
        
        
        current = head
        countNode = 0
        while current:
            countNode += 1
            if countNode == (k-1): break
            current = current.next

        current.next = current.next.next
        return head