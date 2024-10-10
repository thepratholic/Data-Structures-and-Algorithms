class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def InsertAtPosition(head, pos, x):
    temp = Node(x)
    if head is None: return temp
    curr = head
    for i in range(pos - 2):
        if curr is None: return head
        curr = curr.next
    temp.next = curr.next
    curr.next = temp
    return head


def printList(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next

head = None
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
head = InsertAtPosition(head, 5, 45)
printList(head)