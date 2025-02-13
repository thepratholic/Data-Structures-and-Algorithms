class Solution:
    def subarraySum(self, nums, k):
        n = len(nums)
        preSumMap = {0:1}
        cnt = 0
        s = 0

        for i in range(n):
            s += nums[i]
            remove = s - k 
            cnt += preSumMap.get(remove, 0)
            preSumMap[s] = preSumMap.get(s, 0) + 1

        return cnt
