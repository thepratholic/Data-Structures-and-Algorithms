# Definition of doubly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

class Solution:
    def deleteGivenNode(self, node):
        prev = node.prev
        front = node.next

        if front is None:
            prev.next = None
            node.prev = None
            return

        prev.next = front
        front.prev = prev
        node.prev = node.next = None
        