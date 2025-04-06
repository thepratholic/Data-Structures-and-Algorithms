# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getIntersectionNode(self, headA, headB):
        temp1 = headA
        temp2 = headB

        if headA is None or headB is None: return None

        while temp1 != temp2:
            temp1 = temp1.next
            temp2 = temp2.next

            if temp1 == temp2: return temp1
            if temp1 is None: temp1 = headB
            if temp2 is None: temp2 = headA

        return temp1