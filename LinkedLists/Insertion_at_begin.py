class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def InsertAtBegin(head, x):
    temp = Node(x)
    temp.next = head
    return temp
def printList(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
head = None
head = InsertAtBegin(head, 40)
head = InsertAtBegin(head, 30)
head = InsertAtBegin(head, 20)
head = InsertAtBegin(head, 10)
printList(head)