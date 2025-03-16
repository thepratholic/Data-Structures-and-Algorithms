# Definition of doubly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

class Solution:
    def deleteHead(self, head):
        if not head: return None
        if head.next is None: return None
        temp = head
        head = head.next
        temp.next = None
        head.prev = None
        return head