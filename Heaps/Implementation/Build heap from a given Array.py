class Solution:
    def heapify_down(self, nums, ind):
        index = ind
        leftchild_ind = 2 * ind + 1
        rightchild_ind = 2 * ind + 2
        n = len(nums)

        if leftchild_ind < n and nums[index] > nums[leftchild_ind]:
            index = leftchild_ind

        if rightchild_ind < n and nums[index] > nums[rightchild_ind]:
            index = rightchild_ind

        if index != ind:
            nums[index], nums[ind] = nums[ind], nums[index]
            self.heapify_down(nums, index)

        return

    def buildMinHeap(self, nums):
        n = len(nums)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify_down(nums, i)
            