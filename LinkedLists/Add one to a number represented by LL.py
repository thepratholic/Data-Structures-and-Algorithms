# Definition of singly linked list:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def helper(self, temp):
        if temp is None:
            return 1

        carry = self.helper(temp.next)
        temp.val += carry
        if temp.val < 10:
            return 0

        else:
            temp.val = 0
            return 1
            
    def addOne(self, head):

        if head is None: return None
        temp = head
        carry = self.helper(temp)
        if carry == 1:
            newNode = ListNode(1)
            newNode.next = head
            return newNode

        return head