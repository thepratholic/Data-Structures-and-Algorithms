class Solution:
    def merge(self, nums1, m, nums2, n):
        left, right = m - 1, 0

        while left >= 0 and right < n:
            if nums1[left] > nums2[right]:
                nums1[left], nums2[right] = nums2[right], nums1[left]
                left -= 1
                right += 1
            else: 
                break

        nums1[:m] = sorted(nums1[:m])

        nums2.sort()

        for i in range(m, m + n):
            nums1[i] = nums2[i - m]
