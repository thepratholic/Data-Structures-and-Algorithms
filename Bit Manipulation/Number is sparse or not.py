def isSparse(self,n):

        curr, maxi = 0, 0

        while n > 0:
            n &= (n << 1)
            curr += 1
            maxi = max(maxi, curr)

        if maxi > 1:
            return 0
        else:
            return 1