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

def insertAtBegin(head, x):
    temp = Node(x)
    if head is None: return temp

    temp.next = head
    head.prev = temp
    return temp

head = Node(10)
head = insertAtBegin(head, 5)
printList(head)