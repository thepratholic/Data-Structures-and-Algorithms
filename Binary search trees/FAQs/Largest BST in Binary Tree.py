# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    # helper class to get information about the subtree
    class NodeValue:
        def __init__(self, minNode, maxNode, maxSize):
            self.minNode = minNode
            self.maxNode = maxNode
            self.maxSize = maxSize

    def helper(self, root):
        if not root:
            return self.NodeValue(float("inf"), float("-inf"), 0)

        left = self.helper(root.left)
        right = self.helper(root.right)

        if left.maxNode < root.data < right.minNode:
            return self.NodeValue(min(left.minNode, root.data),
                                  max(root.data, right.maxNode), 
                                  left.maxSize + right.maxSize + 1)

        return self.NodeValue(float("-inf"), float("inf"), max(left.maxSize, right.maxSize))



    def largestBST(self, root):
        return self.helper(root).maxSize