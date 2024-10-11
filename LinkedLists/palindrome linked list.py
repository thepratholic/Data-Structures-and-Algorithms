#User function Template for python3
'''
	Your task is to check if given linkedlist
	is a pallindrome or not.

	Function Arguments: head (reference to head of the linked list)
	Return Type: boolean , no need to print just return True or False.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''

class Solution:
    def reverse(self, head):
        if head is None: return None
        cur = head
        prev = None
        while cur is not None:
            nextt = cur.next
            cur.next = prev
            prev = cur
            cur = nextt
        return prev
    def isPalindrome(self, head):
        #code here
        curr1 = head
        curr2 = self.reverse(head)

        while curr1 and curr2:
            if curr1.data != curr2.data:
                return False
            curr1 = curr1.next
            curr2 = curr2.next

        return True