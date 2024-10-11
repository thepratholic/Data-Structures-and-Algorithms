#User function Template for python3


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def deleteTail(head):
    #code here
    if head is None:
        return None

    if head.next == head: return None

    cur = head
    while cur.next.next != head:
        cur = cur.next

    cur.next = cur.next.next
    return head