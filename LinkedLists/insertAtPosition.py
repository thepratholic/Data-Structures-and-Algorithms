class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def InsertAtPosition(head, pos, x):
    temp = Node(x)
    if head is None: return temp
    cnt = 0
    curr = head
    while curr != None:
        cnt += 1
        curr = curr.next
    if pos > cnt: return None
    curr = head
    for i in range(pos-1):
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
head = InsertAtPosition(head, 4, 45)
printList(head)