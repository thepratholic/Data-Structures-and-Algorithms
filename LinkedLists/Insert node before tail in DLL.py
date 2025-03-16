# Definition of doubly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

class Solution:
    def insertBeforeTail(self, head, X):
        if head is None:
            return None

        if head.next is None:
            newNode = ListNode(X, head, None)
            head.prev = newNode
            return newNode

        newNode = ListNode(X)
        current = head

        while current.next is not None:
            current = current.next

        newNode.prev = current.prev
        current.prev = newNode
        newNode.next = current

        newNode.prev.next = newNode
        return head
