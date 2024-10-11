class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None


class Solution:
    #Function to insert a new node at given position in doubly linked list.
    def addNode(self, head, p, x):
        # Code here
        if head is None:
            return None

        current = head
        while current and p > 0:
            current = current.next
            p -= 1

        temp = Node(x)
        temp.next = current.next
        temp.prev = current
        if current.next != None:
            current.next.prev = temp

        current.next = temp
        return head