class Solution:
    def __init__(self):
        self.arr = []
        self.count = 0

    def heapify_up(self, arr, ind):
        parent = (ind - 1) // 2

        if ind > 0 and self.arr[parent] < self.arr[ind]:
            self.arr[parent], self.arr[ind] = self.arr[ind], self.arr[parent]
            self.heapify_up(self.arr, parent)

        return

    def heapify_down(self, arr, ind):
        index = ind
        leftchild_ind = 2 * ind + 1
        rightchild_ind = 2 * ind + 2
        n = len(self.arr)

        if leftchild_ind < n and self.arr[leftchild_ind] > self.arr[index]:
            index = leftchild_ind

        if rightchild_ind < n and self.arr[rightchild_ind] > self.arr[index]:
            index = rightchild_ind

        if index != ind:
            self.arr[index], self.arr[ind] = self.arr[ind], self.arr[index]
            self.heapify_down(self.arr, index)

        return

    def initializeHeap(self):
        self.arr.clear()
        self.count = 0

    def insert(self, key):
        self.arr.append(key)

        self.heapify_up(self.arr, self.count)
        self.count += 1
        return

    def changeKey(self, index, new_val):
        if self.arr[index] > new_val:
            self.arr[index] = new_val
            self.heapify_down(self.arr, index)

        else:
            self.arr[index] = new_val
            self.heapify_up(self.arr, index)

        return

    def extractMax(self):
        ele = self.arr[0]

        self.arr[0], self.arr[len(self.arr) - 1] = self.arr[len(self.arr) - 1], self.arr[0]
        self.arr.pop()
        self.count -= 1

        if self.count > 0:
            self.heapify_down(self.arr, 0)

        return ele

    def isEmpty(self):
        return self.count == 0

    def getMax(self):
        return self.arr[0] if self.count > 0 else None

    def heapSize(self):
        return self.count