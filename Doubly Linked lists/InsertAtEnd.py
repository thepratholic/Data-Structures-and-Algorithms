class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def printList(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next

def insertAtEnd(head, x):
    tmp = Node(x)

    if head is None:
        return tmp

    cur = head
    while cur.next is not None:
        cur = cur.next

    cur.next = tmp
    tmp.prev = cur
    return head

head = Node(10)
head = insertAtEnd(head, 20)
head = insertAtEnd(head, 30)
printList(head)