#User function Template for python3
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Solution:
    def sortedInsert(self, head, x):
    #code here
        temp = Node(x)
        if head is None:
            return temp

        if x <= head.data:
            temp.next = head
            head.prev = temp
            return temp

        current = head
        while current.next and current.next.data < x:
            current = current.next

        temp.next = current.next
        temp.prev = current

        if current.next is not None:
            current.next.prev = temp
        current.next = temp
        return head