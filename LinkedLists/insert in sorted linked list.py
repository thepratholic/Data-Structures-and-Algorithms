#User function Template for python3


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def  insertInSorted(head,data):
    #code here
    tmp = Node(data)
    if head is None: return tmp

    elif data < head.data:
        tmp.next = head
        return tmp

    else:
        cur = head
        while cur.next != None and cur.next.data < data:
            cur = cur.next

        tmp.next = cur.next
        cur.next = tmp
        return head