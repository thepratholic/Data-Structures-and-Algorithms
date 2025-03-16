# Definiton of singly Linked List
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertAtTail(self, head, X):
        newNode = ListNode(X)

        if head is None: 
            return newNode

        currentNode = head
        while currentNode.next is not None:
            currentNode = currentNode.next

        currentNode.next = newNode
        return head