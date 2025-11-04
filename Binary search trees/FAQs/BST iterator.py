# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self.pushAll(root)

    
    def hasNext(self):
        return len(self.stack) > 0
    
    def next(self):
        temp_node = self.stack.pop()
        self.pushAll(temp_node.right)
        return temp_node.data

    def pushAll(self, root): # helper function
        while root:
            self.stack.append(root)
            root = root.left

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
