class Solution:
    def subarraysWithXorK(self, nums, k):
        n = len(nums)
        cnt = 0
        xr = 0
        mpp = {0:1}

        for i in range(n):
            xr ^= nums[i]
            x = xr ^ k 
            cnt += mpp.get(x, 0)
            mpp[xr] = mpp.get(xr, 0) + 1

        return cnt