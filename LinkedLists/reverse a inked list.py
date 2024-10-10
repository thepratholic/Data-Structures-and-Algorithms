#function Template for python3

"""
# Node Class

class node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""

class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        if head is None:
            return None

        prev, curr = None, head
        while curr != None:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        return prev