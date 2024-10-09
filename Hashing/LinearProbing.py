class Solution:
    def linearProbing(self,hashSize, arr, n):
        #Your code here
        hashTable = [-1 for i in range(hashSize)]

        for i in arr:
            h = i % hashSize
            original_index = h


            while hashTable[h] != -1:
                if hashTable[h] == i:
                    break
                h = (h+1) % hashSize

                if h == original_index:
                    break
            if hashTable[h] == -1:
                hashTable[h] = i
                
        return hashTable
    