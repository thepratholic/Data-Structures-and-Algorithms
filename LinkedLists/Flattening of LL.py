# Definiton of singly Linked List
class ListNode:
    def __init__(self, val=0, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child

class Solution:
    def merge(self, list1, list2):
        dummyNode = ListNode(-1)
        res = dummyNode

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                res.child = list1
                res = list1
                list1 = list1.child
            else:
                res.child = list2
                res = list2
                list2 = list2.child

        if list1:
            res.child = list1
        else:
            res.child = list2

        return dummyNode.child


    def flattenLinkedList(self, head):
        if head is None or head.next is None:
            return head

        mergedHead = self.flattenLinkedList(head.next)
        return self.merge(head, mergedHead)
