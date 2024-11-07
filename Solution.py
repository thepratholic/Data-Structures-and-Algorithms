class Solution:
    def findPath(self, A, B):
        MOD = (10**9) + 7
        i, j = 0, 0
        sumA, sumB = 0, 0
        result = 0

        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                sumA += A[i]
                i += 1
            elif B[j] < A[i]:
                sumB += B[j]
                j += 1
            else:  # A[i] == B[j]
                result += max(sumA, sumB) + A[i]
                result %= MOD  # Take MOD to prevent overflow
                sumA = sumB = 0  # Reset sums in this case
                i += 1
                j += 1

        # Adding remaining elements from both paths, if in case there are some elements left
        while i < len(A):
            sumA += A[i]
            i += 1
        while j < len(B):
            sumB += B[j]
            j += 1

        result += max(sumA, sumB)
        result %= MOD

        return result

s = Solution()
print(s.findPath([1,3,5,7,9], [3, 5, 100]))