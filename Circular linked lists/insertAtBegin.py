class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printList(head):
    if head is None: return None

    print(head.data, end=" ")

    curr = head.next

    while curr != head:
        print(curr.data, end=" ")
        curr = curr.next

def insertInHead(head,x):
    #code here
    
    temp = Node(x)
    if head is None:
        temp.next = temp
        return temp
        
    temp.next = head.next
    head.next = temp
    temp.data, head.data = head.data, temp.data
    return head

head = Node(10)
head.next = Node(20)
head.next.next = head
head = insertInHead(head, 5)
printList(head)