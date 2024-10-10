#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
def searchLinkedList(head,x):
    #code here
    pos = 1
    curr = head
    while curr:
        if curr.data == x:
            return pos
        pos += 1
        curr = curr.next
    return -1