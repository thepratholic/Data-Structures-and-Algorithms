
# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseLinkedList(self, temp):
        prev =  None
        # temp = head
        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev

    def getKthNode(self, temp, k):
        k -= 1
        while temp is not None and k > 0:
            k -= 1
            temp = temp.next
        return temp

    def reverseKGroup(self, head, k):
        temp = head
        if temp is None: return None

        prevNode = None
        while temp is not None:
            kThNode = self.getKthNode(temp, k)

            if kThNode is None:
                if prevNode: 
                    prevNode.next = temp
                    break
            
            nextNode = kThNode.next
            kThNode.next = None
            self.reverseLinkedList(temp)

            if temp == head:
                head = kThNode
            else:
                prevNode.next = kThNode
            
            prevNode = temp
            temp = nextNode
        return head

