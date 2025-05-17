class Solution:
    def findPlatform(self, arrival, departure):
        #your code goes here

        arrival.sort()
        departure.sort()

        i, j = 0, 0
        count, max_count = 0, 0

        n, m = len(arrival), len(departure)

        while i < n:
            if arrival[i] <= departure[j]:
                count += 1
                i += 1

            else:
                count -= 1
                j += 1

            max_count = max(max_count, count)

        return max_count
