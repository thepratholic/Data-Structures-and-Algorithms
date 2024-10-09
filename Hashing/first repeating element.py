class Solution:
    #Function to return the position of the first repeating element.
    def firstRepeated(self,arr):
        #arr : given array
        #n : size of the array
        n = len(arr)
        
        d = {}
        smallest_indexes = {}

        for i in arr:
            if i not in d:
                d[i] = 1
            else: d[i] += 1

        for i in range(n):
            if arr[i] not in smallest_indexes:
                smallest_indexes[arr[i]] = i+1
            else:
                smallest_indexes[arr[i]] = min(i+1, smallest_indexes[arr[i]])
        
        for i in arr:
            if d[i] > 1:
                return smallest_indexes[i]
        return -1
        

s = Solution()
print(s.firstRepeated([1, 2, 3, 4]))