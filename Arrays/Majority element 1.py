class Solution:
    def majorityElement(self, nums):
        cnt, el = 0, -1
        n = len(nums)

        for i in range(n):
            if cnt == 0:
                el = nums[i]
                cnt = 1

            elif nums[i] == el: cnt += 1
            else: cnt -= 1

        cnt1 = nums.count(el)

        if cnt1 > (n // 2): return el

        return -1