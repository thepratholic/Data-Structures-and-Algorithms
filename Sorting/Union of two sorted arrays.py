class Solution:
    def findUnion(self,arr1,arr2,n,m):
        i, j = 0, 0
        union = []

        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:  # Case 1 and 2
                if len(union) == 0 or union[-1] != arr1[i]:
                    union.append(arr1[i])
                i += 1
            else:
                if len(union) == 0 or union[-1] != arr2[j]:
                    union.append(arr2[j])
                j += 1

        while i < len(arr1):
            if union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1

        while j < len(arr2):
            if union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1

        return union

s = Solution()
print(s.findUnion([1,2,4,5,6],[2,4,4,6,8],5,5))