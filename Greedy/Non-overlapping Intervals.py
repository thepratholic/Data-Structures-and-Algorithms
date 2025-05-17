class Solution:
    def MaximumNonOverlappingIntervals(self, intervals):
        #your code goes here
        n = len(intervals)
        intervals.sort(key = lambda x : x[1])
        last_end_time = intervals[0][1]
        count = 1

        for i in range(1, n):
            if intervals[i][0] >= last_end_time:
                count += 1
                last_end_time = intervals[i][1]

        return n - count