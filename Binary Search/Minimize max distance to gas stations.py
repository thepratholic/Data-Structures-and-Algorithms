class Solution:
    def numberOfGasStationsRequired(self, dist, arr):
        n = len(arr)
        cnt = 0
        for i in range(1, n):
            # Calculate number of gas stations 
            # needed between two points
            numberInBetween = (arr[i] - arr[i - 1]) / dist
            
            # Adjust if exact distance fits perfectly
            if (arr[i] - arr[i - 1]) == (dist * int(numberInBetween)):
                numberInBetween -= 1

            cnt += int(numberInBetween)
        return cnt

    # Function to minimize the maximum 
    # distance between gas stations
    def minimiseMaxDistance(self, arr, k):
        n = len(arr)
        low = 0
        high = 0

        # Find the maximum distance between 
        # consecutive gas stations
        for i in range(n - 1):
            high = max(high, arr[i + 1] - arr[i])

        # Apply Binary search to find the
        # minimum possible maximum distance
        diff = 1e-6
        while high - low > diff:
            mid = (low + high) / 2.0
            cnt = self.numberOfGasStationsRequired(mid, arr)

            # Adjust the search range based on the
            # number of gas stations required
            if cnt > k:
                low = mid
            else:
                high = mid

        # Return the smallest maximum distance found
        return high