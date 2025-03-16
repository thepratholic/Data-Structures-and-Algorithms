# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def LLTraversal(self, head):
        temp = head
        arr = []
        while temp:
            arr.append(temp.val)
            temp = temp.next

        return arr