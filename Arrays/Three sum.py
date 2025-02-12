class Solution:
    def threeSum(self, nums):
        n = len(nums)
        ans = []
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]: continue

            j, k = i + 1, n - 1
            while j < k:
                sums = nums[i] + nums[j] + nums[k]

                if sums < 0: j += 1
                elif sums > 0: k -= 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while(j < k and nums[j] == nums[j - 1]): j += 1
                    while(j < k and nums[k] == nums[k + 1]): k -= 1

        return ans