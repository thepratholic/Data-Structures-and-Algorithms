# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def isLeaf(self, root):
        return not root.left and not root.right

    def addLeftBoundary(self, root, ans):
        current = root.left
        while current:
            if not self.isLeaf(current):
                ans.append(current.data)
            if current.left:
                current = current.left
            else:
                current = current.right

    def addLeaves(self, root, ans):
        if self.isLeaf(root):
            ans.append(root.data)
            return
        
        if root.left:
            self.addLeaves(root.left, ans)
        if root.right:
            self.addLeaves(root.right, ans)

    def addRightBoundary(self, root, ans):
        curr = root.right
        tmp = []
        while curr:
            if not self.isLeaf(curr):
                tmp.append(curr.data)

            if curr.right:
                curr = curr.right
            else:
                curr = curr.left

        ans.extend(tmp[::-1])

    def boundary(self, root):
        ans = []
        if not root:
            return ans
        
        if not self.isLeaf(root):
            ans.append(root.data)

        self.addLeftBoundary(root, ans)
        self.addLeaves(root, ans)
        self.addRightBoundary(root, ans)
        return ans