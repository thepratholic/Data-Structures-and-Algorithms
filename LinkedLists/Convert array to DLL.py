# Definition of doubly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

class Solution:
    def arrayToLinkedList(self, nums):
        if not nums: return None
        head = ListNode(nums[0])

        prev = head

        for i in range(1, len(nums)):
            temp = ListNode(nums[i], None, prev)
            prev.next = temp
            prev = prev.next
        return head
