# Definition of doubly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

class Solution:
    def deleteKthElement(self, head, k):
        if head is None:
            return None

        node_count = 0
        current_node = head

        while current_node.next is not None:
            node_count += 1
            if node_count == k:
                break
            current_node = current_node.next

        prev = current_node.prev
        front = current_node.next

        if prev is None and front is None:
            return None

        elif prev is None:
            head = front
            front.prev = None

        elif front is None:
            prev.next = None

        else:
            prev.next = front
            front.prev = prev

        return head