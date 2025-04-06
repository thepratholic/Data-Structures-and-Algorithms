# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head, k):
        if head is None: return None

        length = 1
        tail = head
        while tail.next is not None:
            length += 1
            tail = tail.next

        if k % length == 0: return head
        tail.next = head
        k = k % length

        newLastNode = length - k 
        while newLastNode > 0:
            tail = tail.next
            newLastNode -= 1

        head = tail.next
        tail.next = None
        return head
