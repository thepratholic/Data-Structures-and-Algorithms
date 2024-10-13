# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findPerfectSubtreeSizes(self, root):
        perfect_sizes = []


        def helper(node):
            if not node:
                return True, 0, 0


            left_is_perfect, left_height, left_size = helper(node.left)
            right_is_perfect, right_height, right_size = helper(node.right)


            if left_is_perfect and right_is_perfect and left_height == right_height:

                height = left_height + 1

                size = left_size + right_size + 1
                perfect_sizes.append(size)
                return True, height, size
            else:

                return False, 0, 0


        helper(root)

        return perfect_sizes
    def kthLargestPerfectSubtree(self, root, k: int) -> int:
        perfect_sizes = self.findPerfectSubtreeSizes(root)

        perfect_sizes.sort(reverse=True)

        if len(perfect_sizes) >= k:
            return perfect_sizes[k - 1]
        else:
            return -1