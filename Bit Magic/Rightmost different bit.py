def posOfRightMostDiffBit(self,m,n):

        ans = m ^ n
        if ans == 0: return -1
        pos = 0
        while ans & 1 == 0:
            ans >>= 1
            pos += 1
        return pos + 1