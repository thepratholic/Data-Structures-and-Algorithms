# Definition of doubly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

class Solution:
    def removeDuplicates(self, head):
        if head is None:
            return None

        temp = head
        while temp.next is not None:
            nextNode = temp.next

            while nextNode != None and nextNode.val == temp.val:
                duplicate = nextNode
                nextNode = nextNode.next
                del duplicate

            temp.next = nextNode
            if nextNode: 
                nextNode.prev = temp 

            temp = temp.next
        return head