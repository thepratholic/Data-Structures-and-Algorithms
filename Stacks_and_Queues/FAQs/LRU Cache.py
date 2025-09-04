class Node:
  def __init__(self, key = -1, val = -1):
    self.key = key
    self.val = val
    self.next = None
    self.prev = None

class LRUCache:
  def __init__(self, capacity):
    self.size = capacity
    self.mpp = {}
    self.head = Node()
    self.tail = Node()

    self.head.next = self.tail
    self.tail.prev = self.head

  def insertAfterHead(self, node):
    node.next = self.head.next
    node.next.prev = node
    node.prev = self.head
    self.head.next = node

  def deleteNode(self, node):
    prevNode = node.prev
    nextNode = node.next

    prevNode.next = nextNode
    nextNode.prev = prevNode

  def get(self, key_):
    if key_ not in self.mpp:
      return -1

    node = self.mpp[key_]
    value = node.val
    
    self.deleteNode(node)
    self.insertAfterHead(node)

    return value

  def put(self, key_, value):
    if key_ in self.mpp:
      node = self.mpp[key_]
      node.val = value
      self.deleteNode(node)
      self.insertAfterHead(node)
      return

    if len(self.mpp) == self.size:
      node = self.tail.prev
      del self.mpp[node.key]
      self.deleteNode(node)

    newNode = Node(key_, value)
    self.mpp[key_] = newNode

    self.insertAfterHead(newNode)
       