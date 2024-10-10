#User function Template for python3
'''
	A linked list node has the following structure
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
#Function to find the data of kth node from the end of a linked list
class Solution:
    def getKthFromLast(self, head, k):
        #code here
        if head is None: return None
        first, second = head, head
        for i in range(k):
            if first is None: return -1
            first = first.next

        while first != None:
            first = first.next
            second = second.next
        return second.data if second else -1