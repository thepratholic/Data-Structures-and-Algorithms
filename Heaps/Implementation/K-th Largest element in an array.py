from random import randint

class Solution:
    def randomIndex(self, left, right):
        length = right - left + 1
        return randint(left, right)

    def kthLargestElement(self, nums, k):
        n = len(nums)
        l, r = 0, n - 1

        if k > n:
            return -1

        while True:
            pivot_index = self.randomIndex(l, r)

            pivot_index = self.partition_and_return_index(nums, pivot_index, l, r)

            if pivot_index == k-1:
                return nums[pivot_index]

            elif k-1 < pivot_index:
                r = pivot_index - 1

            else:
                l = pivot_index + 1

    def partition_and_return_index(self, nums, pivot_index, left, right):
        pivot = nums[pivot_index]

        nums[pivot_index], nums[left] = nums[left], nums[pivot_index]

        ind = left + 1

        for i in range(left + 1, right + 1):
            if nums[i] > pivot:
                nums[i], nums[ind] = nums[ind], nums[i]
                ind += 1

        nums[ind - 1], nums[left] = nums[left], nums[ind - 1]
        return ind - 1
        