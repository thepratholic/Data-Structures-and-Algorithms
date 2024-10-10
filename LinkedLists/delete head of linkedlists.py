#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

def deleteHead(head):
    #code here
    if head == None:
        return None
    else:
        tmp = head
        head = head.next
        tmp.next = None
        return head