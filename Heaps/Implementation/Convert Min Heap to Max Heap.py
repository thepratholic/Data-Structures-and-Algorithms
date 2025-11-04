class Solution:
    def heapify_down(self, arr, ind):
        index = ind
        n = len(arr)
        leftchild_ind = 2 * ind + 1
        rightchild_ind = 2 * ind + 2

        if leftchild_ind < n and arr[leftchild_ind] > arr[index]:
            index = leftchild_ind

        if rightchild_ind < n and arr[rightchild_ind] > arr[index]:
            index = rightchild_ind

        if index != ind:
            arr[index], arr[ind] = arr[ind], arr[index]
            self.heapify_down(arr, index)
        return

    def minToMaxHeap(self, nums):
        n = len(nums)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify_down(nums, i)

        return nums