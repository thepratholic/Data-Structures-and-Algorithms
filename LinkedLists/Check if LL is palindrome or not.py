# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        if head is None: return None
        if head.next is None: return head
        prev = None
        temp = head
        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev
        
    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True

        # first step to determine the second half by using tortoise and hare algorithm
        slow, fast = head, head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        # second step is to reverse the second half and get new node
        second_head = self.reverseList(slow.next)

        # third step is to compare the nodes of both halves
        first = head
        second = second_head
        while second is not None:
            if first.val != second.val:
                self.reverseList(second_head)
                return False

            first = first.next
            second = second.next
        
        self.reverseList(second_head)
        return True