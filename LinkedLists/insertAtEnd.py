class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def InsertAtEnd(head, x):
    if head == None:
        return Node(x)
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = Node(x)
    return head


def printList(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next

head = None
head = InsertAtEnd(head, 10)
head = InsertAtEnd(head, 20)
head = InsertAtEnd(head, 30)
head = InsertAtEnd(head, 40)
printList(head)