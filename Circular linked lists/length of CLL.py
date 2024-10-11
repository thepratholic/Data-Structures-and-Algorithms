#User function Template for python3


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def getLength(head):
    #code here
    if head is None: return None
    
    # if head.next: return 1
    
    cnt = 1
    curr = head.next
    
    while curr != head:
        cnt += 1
        curr = curr.next
        
    return cnt