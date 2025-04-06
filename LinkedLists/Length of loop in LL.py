# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findLengthOfLoop(self, slow, fast):
        cnt = 1
        fast = fast.next
        while fast != slow:
            cnt += 1
            fast = fast.next
        return cnt
        
    def findLengthOfLoop(self, head):
        if head is None: return None
        
        slow, fast = head, head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return self.findLengthOfLoop(slow, fast)

        return 0