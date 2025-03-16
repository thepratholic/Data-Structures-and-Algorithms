# Definition of doubly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

class Solution:
    def insertBeforeGivenNode(self, node, X):
        newNode = ListNode(X)

        newNode.prev = node.prev
        node.prev = newNode
        newNode.next = node
        newNode.prev.next = newNode
        