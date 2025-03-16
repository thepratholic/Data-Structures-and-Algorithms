# Definition of doubly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

class Solution:
    def insertBeforeKthPosition(self, head, X, k):
        if head is None: return None

        if k == 1:
            newNode = ListNode(X, head, None)
            head.prev = newNode
            return newNode
        
        node_count = 0
        current_node = head
        while current_node.next is not None:
            node_count += 1
            if node_count == k:
                break
            current_node = current_node.next

        newNode = ListNode(X, current_node, current_node.prev)
        current_node.prev = newNode
        newNode.prev.next = newNode
        return head