# Definition of singly linked list:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def findMiddle(self, head):
        slow, fast = head, head.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, list1, list2):
        dummyNode = ListNode(-1)
        temp = dummyNode
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                temp.next = list1
                temp = list1
                list1 = list1.next
            else:
                temp.next = list2
                temp = list2
                list2 = list2.next

        if list1:
            temp.next = list1
        else:
            temp.next = list2

        return dummyNode.next

    def sortList(self, head):
        if head is None or head.next is None:
            return head

        middle = self.findMiddle(head)
        leftHead = head
        rightHead = middle.next
        middle.next = None

        leftHead = self.sortList(leftHead)
        rightHead = self.sortList(rightHead)

        return self.merge(leftHead, rightHead)