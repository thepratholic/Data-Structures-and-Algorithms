class Solution:
    def kthElement(self, arr1, arr2, k):
        m, n = len(arr1), len(arr2)
        if m > n: 
            return self.kthElement(arr2, arr1, k)

        left = k
        low, high = max(k-n, 0), min(k, m)

        while low <= high:
            mid1 = (low + high) >> 1
            mid2 = left - mid1

            l1 = arr1[mid1-1] if mid1-1 >= 0 else float("-inf")
            l2 = arr2[mid2 - 1] if mid2-1 >= 0 else float("-inf")
            r1 = arr1[mid1] if mid1 < m else float("inf")
            r2 = arr2[mid2] if mid2 < n else float("inf")

            if (l1 <= r2) and (l2 <= r1):
                    return max(l1, l2)

            elif l1 > r2:
                high = mid1 - 1

            else:
                low = mid1 + 1

        return -1