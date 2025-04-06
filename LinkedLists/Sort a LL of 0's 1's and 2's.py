# Definition of singly linked list:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head):
        if head is None: return None

        if head.next is None: return head

        zeroHead = ListNode(-1)
        zero = zeroHead
        oneHead = ListNode(-1)
        one = oneHead
        twoHead = ListNode(-1)
        two = twoHead
        temp = head

        while temp is not None:
            if temp.val == 0:
                zero.next = temp
                zero = zero.next

            elif temp.val == 1:
                one.next = temp
                one = one.next

            else:
                two.next = temp
                two = two.next

            temp = temp.next

        zero.next = oneHead.next if oneHead.next else twoHead.next
        one.next = twoHead.next
        two.next = None
        newHead = zeroHead.next
        return newHead