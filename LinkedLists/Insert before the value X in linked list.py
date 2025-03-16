# Definiton of singly Linked List
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertBeforeX(self, head, X, val):
        newNode = ListNode(val)

        if head is None: return None
        if head.val == X:
            newNode.next = head
            head = newNode
            return head

        current_node = head
        while current_node.next:
            if current_node.next.val == X:
                newNode.next = current_node.next
                current_node.next = newNode
                break
            current_node = current_node.next
        
        return head