class Solution:
    def majorityElementTwo(self, nums):
        cnt1, cnt2, el1, el2 = 0, 0, -1, -1
        n = len(nums)

        for i in range(n):
            if cnt1 == 0 and nums[i] != el2:
                cnt1 = 1
                el1 = nums[i]

            elif cnt2 == 0 and nums[i] != el1:
                cnt2 = 1
                el2 = nums[i]

            elif nums[i] == el1: cnt1 += 1
            elif nums[i] == el2: cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1, cnt2 = 0, 0
        for num in nums:
            if num == el1: cnt1 += 1
            if num == el2: cnt2 += 1
        
        mini = n // 3 + 1
        res = []
        if cnt1 >= mini:
            res.append(el1)

        if cnt2 >= mini and el1 != el2:
            res.append(el2)

        return res

