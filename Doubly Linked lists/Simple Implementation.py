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

head = Node("A")
temp1 = Node("B")
temp2 = Node("C")

head.next = temp1
temp1.prev = head

temp1.next = temp2
temp2.prev = temp1

printList(head)