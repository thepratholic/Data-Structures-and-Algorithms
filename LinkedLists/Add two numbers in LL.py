# Definiton of singly Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1, l2):
        temp1, temp2 = l1, l2
        dummy = ListNode(-1)
        carry = 0
        curr = dummy

        while temp1 is not None or temp2 is not None:
            s = 0

            if temp1:
                s += temp1.val
                temp1 = temp1.next
            if temp2:
                s += temp2.val
                temp2 = temp2.next

            s += carry
            carry = s//10
            newNode = ListNode(s % 10)

            curr.next = newNode
            curr = newNode

        if carry:
            newNode = ListNode(carry)
            curr.next = newNode

        return dummy.next