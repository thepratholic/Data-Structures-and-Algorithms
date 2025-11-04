class Solution:
    def __init__(self):
        self.arr = []
        self.count = 0

    def heapify_up(self, arr, ind):
        parent = (ind - 1) // 2

        if ind > 0 and arr[ind] < arr[parent]:
            arr[ind], arr[parent] = arr[parent], arr[ind]
            self.heapify_up(arr, parent)

        return

    def heapify_down(self, arr, ind):
        index = ind
        leftchild_ind = 2 * ind + 1
        rightchild_ind = 2 * ind + 2

        if leftchild_ind < len(arr) and arr[leftchild_ind] < arr[index]:
            index = leftchild_ind

        if rightchild_ind < len(arr) and arr[rightchild_ind] < arr[index]:
            index = rightchild_ind

        if index != ind:
            arr[index], arr[ind] = arr[ind], arr[index]
            self.heapify_down(arr, index)

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
            self.heapify_up(self.arr, index)

        else:
            self.arr[index] = new_val
            self.heapify_down(self.arr, index)

    def extractMin(self):
        ele = self.arr[0]

        self.arr[0], self.arr[len(self.arr) - 1] = self.arr[len(self.arr) - 1], self.arr[0]
        self.arr.pop()
        self.count -= 1
        if self.count > 0:
            self.heapify_down(self.arr, 0)

    def isEmpty(self):
        return self.count == 0

    def getMin(self):
        return self.arr[0]

    def heapSize(self):
        return self.count