class Solution:
    def intersectionArray(self, a, b):
        n, m, i, j = len(a), len(b), 0, 0
        intersection = []
        while i < n and j < m:
            if a[i] < b[j]: i += 1
            elif b[j] < a[i]: j += 1
            else:
                intersection.append(a[i])
                i += 1
                j += 1

        return intersection