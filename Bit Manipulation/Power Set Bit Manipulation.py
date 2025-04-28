class Solution:
    def powerSet(self, nums):
        #your code goes here
        n = len(nums)
        answer = []
        for num in range(1 << n):
            current_subset = []
            for i in range(n):
                if num & (1 << i):
                    current_subset.append(nums[i])

            answer.append(current_subset)

        return answer