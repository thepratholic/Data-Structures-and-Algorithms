class Solution:
    def heapify_down(self, arr, last, ind):
        index = ind
        leftchild_ind = 2 * ind + 1
        rightchild_ind = 2 * ind + 2

        if leftchild_ind <= last and arr[leftchild_ind] > arr[index]:
            index = leftchild_ind

        if rightchild_ind <= last and arr[rightchild_ind] > arr[index]:
            index = rightchild_ind

        if index != ind:
            arr[index], arr[ind] = arr[ind], arr[index]
            self.heapify_down(arr, last, index)

        return

    def buildMaxHeap(self, nums):
        n = len(nums)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify_down(nums, n - 1, i)

        return


    def heapSort(self, nums):
        self.buildMaxHeap(nums)

        last = len(nums) - 1

        while last > 0:
            nums[0], nums[last] = nums[last], nums[0]
            last -= 1
            if last > 0:
                self.heapify_down(nums, last, 0)

        return