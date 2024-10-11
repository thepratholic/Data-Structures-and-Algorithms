#User function Template for python3


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteAtPosition(head,pos):
    #code here

    if head is None: return None

    if pos == 1:
        head.data = head.next.data
        head.next = head.next.next
        return head

    cur = head
    for i in range(pos - 2):
        cur = cur.next

    cur.next = cur.next.next
    return head