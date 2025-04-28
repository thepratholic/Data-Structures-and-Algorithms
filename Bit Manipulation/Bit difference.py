def countBitsFlip(self,a,b):
        ##Your code here
        ans = a ^ b
        cnt = 0
        while ans:
            if ans & 1 == 1:
                cnt += 1
                ans >>= 1
            else:
                ans >>= 1

        return cnt