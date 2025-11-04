import heapq
class KthLargest:
    def __init__(self, k, nums):
        self.K = k 
        self.pq = []
        n = len(nums)

        for i in range(n):
            if len(self.pq) < self.K:
                heapq.heappush(self.pq, nums[i])

            elif nums[i] > self.pq[0]:
                heapq.heappop(self.pq)
                heapq.heappush(self.pq, nums[i])

    def add(self, val):
        if len(self.pq) < self.K:
            heapq.heappush(self.pq, val)

        elif val > self.pq[0]:
            heapq.heappop(self.pq)
            heapq.heappush(self.pq, val)

        return self.pq[0]