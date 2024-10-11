#User function Template for python3
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertAtPosition(head,pos,data):
    #code here
    temp = Node(data)
    if head is None:
        return None

    count = 1
    curr = head
    while count < pos and curr.next != head:
        count+=1
        curr = curr.next

    if count == pos:
        temp.next = curr.next
        curr.next = temp

    return head