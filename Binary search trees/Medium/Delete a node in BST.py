# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def rightMost(self, root):
        while root:
            if not root.right:
                return root
            root = root.right

    def helper(self, root, key):
        if not root.left:
            return root.right

        elif not root.right:
            return root.left

        else:
            right_child = root.right
            right_most_child_in_left_subtree = self.rightMost(root.left)
            right_most_child_in_left_subtree.right = right_child
            return root.left

    def deleteNode(self, root, key):
        if not root:
            return None

        if root.data == key:
            return self.helper(root, key)

        dummy = root

        while root:
            if root.data > key:
                if root.left and root.left.data == key:
                    root.left = self.helper(root.left, key)
                    break

                else:
                    root = root.left

            else:
                if root.right and root.right.data == key:
                    root.right = self.helper(root.right, key)
                    break
                else:
                    root = root.right

        return dummy

    