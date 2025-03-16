# Definiton of singly Linked List
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertAtHead(self, head, X):
        currentNode = ListNode(X)

        currentNode.next = head
        head = currentNode
        return head