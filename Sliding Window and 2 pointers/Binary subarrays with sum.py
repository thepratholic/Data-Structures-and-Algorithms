class Solution:
    def f(self, nums, goal):
        if goal < 0: return 0
        n, l, r, summ, cnt = len(nums), 0, 0, 0, 0

        while r < n:
            summ += nums[r]
            while summ > goal:
                summ -= nums[l]
                l+=1

            cnt += (r - l + 1)
            r += 1
        return cnt

    def binarySubarrays(self, nums, goal):
        return self.f(nums, goal) - self.f(nums, goal - 1)

s = Solution()
print(s.binarySubarrays([1, 0, 1, 0, 1], 2))