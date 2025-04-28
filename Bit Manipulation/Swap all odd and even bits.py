def swapBits(self,n):
        #Your code here
        EVEN_MASK = 0xAAAAAAAA
        ODD_MASK  = 0x55555555

        evenBits = (n & EVEN_MASK) >> 1
        oddBits = (n & ODD_MASK) << 1

        ans = evenBits | oddBits
        return ans