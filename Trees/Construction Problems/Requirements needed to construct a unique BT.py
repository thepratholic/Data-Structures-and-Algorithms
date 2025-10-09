class Solution:
    def unique_binary_tree(self, a, b):
        return (a == 2 or b == 2) and (a != b)