class Solution:
    def missingPanagram(self, s):
        s = s.lower()
        alphabet_set = set('abcdefghijklmnopqrstuvwxyz')

        for char in s:
            alphabet_set.discard(char)

        if not alphabet_set:
            return -1
        return ''.join(sorted(alphabet_set))