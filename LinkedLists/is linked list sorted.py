#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
def isSorted(head):
    #code here
    if head is None or head.next is None: return 1
    curr = head

    is_dec = True
    is_inc = True

    while curr.next:
        if curr.data < curr.next.data:
            is_dec = False
        elif curr.data > curr.next.data:
            is_inc = False
        curr = curr.next

    return 1 if is_inc or is_dec else 0