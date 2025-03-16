# Definition of doubly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

class Solution:
    def deleteTail(self, head):
        if not head: return None

        if head.next is None: return None

        current_node = head

        while current_node.next.next is not None:
            current_node = current_node.next

        current_node.next.prev = None
        current_node.next = None
        return head