from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def serialize(self, root):
        if not root:
            return ""

        result = []
        q = deque([root])

        while q:
            node = q.popleft()

            if node is None:
                result.append("#")
            else:
                result.append(str(node.data))
                q.append(node.left)
                q.append(node.right)

        return ",".join(result)

    def deserialize(self, data):
        if not data:
            return None

        data = deque(data.split(","))
        root = TreeNode(int(data.popleft()))

        q = deque([root])
        while q:
            node = q.popleft()

            left_val = data.popleft()
            if left_val != "#":
                left_node = TreeNode(int(left_val))
                node.left = left_node
                q.append(left_node)

            right_val = data.popleft()
            if right_val != "#":
                right_node = TreeNode(int(right_val))
                node.right = right_node
                q.append(right_node)

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans