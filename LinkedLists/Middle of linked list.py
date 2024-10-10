class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printList(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next

def middle(head):
    if head == None: return None
    slow, fast = head, head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    return slow.data


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
# printList(head)
print(middle(head))