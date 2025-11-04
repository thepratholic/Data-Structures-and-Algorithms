class Solution:
    def heapify_up(self, nums, ind):
        parent = (ind - 1) // 2

        if ind > 0 and nums[parent] > nums[ind]:
            nums[parent], nums[ind] = nums[ind], nums[parent]
            self.heapify_up(nums, parent)

        return

    def heapify_down(self, nums, ind):
        index = ind
        leftchild_ind = 2 * ind + 1
        rightchild_ind = 2 * ind + 2

        if leftchild_ind < len(nums) and nums[index] > nums[leftchild_ind]:
            index = leftchild_ind

        if rightchild_ind < len(nums) and nums[index] > nums[rightchild_ind]:
            index = rightchild_ind

        if index != ind:
            nums[index], nums[ind] = nums[ind], nums[index]
            self.heapify_down(nums, index)

        return


    def heapify(self, nums, ind, val):
        if nums[ind] > val:
            nums[ind] = val
            self.heapify_up(nums, ind)

        else:
            nums[ind] = val
            self.heapify_down(nums, ind)

        return         