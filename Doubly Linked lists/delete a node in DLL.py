class Solution:
    def delete_node(self, head, x):
        #code here
        if head is None: return None
        if x == 1:
            head = head.next
            head.prev = None
            return head

        temp = head
        for i in range(x-1):
            if temp.next is None:
                return head
            temp = temp.next

        temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.prev

        return head