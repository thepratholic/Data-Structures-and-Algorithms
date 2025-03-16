# Definiton of singly Linked List
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertAtKthPosition(self, head, X, k):
        newNode = ListNode(X)

        if head is None:
            return newNode

        if k == 1:
            newNode.next = head
            head = newNode
            return head

        currentNode = head
        nodeCount = 0

        while currentNode:
            nodeCount += 1
            if nodeCount == (k-1):
                newNode.next = currentNode.next
                currentNode.next = newNode
                break
            currentNode = currentNode.next

        return head