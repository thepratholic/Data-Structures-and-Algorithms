class Solution:
    def twoSum(self, nums, target):
        n = len(nums)

        ans = [-1, -1]

        freq = []

        for i in range(n):
            freq.append([nums[i], i])

        freq.sort(key=lambda x:x[0])

        left, right = 0, n-1
        while left < right:
            sum_val = freq[left][0] + freq[right][0]

            if sum_val == target:
                ans[0] = freq[left][1]
                ans[1] = freq[right][1]
                return ans
            
            elif sum_val > target:
                right -= 1

            else: left += 1

        return ans