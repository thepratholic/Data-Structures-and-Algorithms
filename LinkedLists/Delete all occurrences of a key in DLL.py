# Definition of doubly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

class Solution:
    def deleteAllOccurrences(self, head, target):
        if head is None:
            return None

        temp = head

        while temp is not None:
            if temp.val == target:
                if temp == head:
                    head = head.next

                prevNode = temp.prev
                nextNode = temp.next

                if prevNode:
                    prevNode.next = nextNode
                if nextNode:
                    nextNode.prev = prevNode

                temp = nextNode
            else:
                temp = temp.next
        return head