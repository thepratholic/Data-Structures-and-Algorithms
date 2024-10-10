class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteAtPosition(head, pos):
    #code here
    if head is None: return None
    if pos == 1:
        return head.next

    cnt = 1
    curr = head
    while curr is not None and cnt < pos-1:
        curr = curr.next
        cnt += 1

    curr.next = curr.next.next

    return head