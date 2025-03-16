# Definition of doubly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

class Solution:
    def insertBeforeHead(self, head, X):
        newNode = ListNode(X)

        newNode.next = head
        head.prev = newNode
        head = newNode
        return head