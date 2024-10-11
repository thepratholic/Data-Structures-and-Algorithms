class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printList(head):
    if head is None: return None

    print(head.data)

    curr = head.next

    while curr != head:
        print(curr.data, end=" ")
        curr = curr.next

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head
printList(head)