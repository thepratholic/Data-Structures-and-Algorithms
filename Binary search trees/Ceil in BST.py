class Solution:
    def findCeil(self,root, inp):
        # code here
        res = -1
        while root is not None:
            if root.key == inp:
                return root.key

            elif inp < root.key:
                res = root.key
                root = root.left

            else:
                root = root.right

        return res