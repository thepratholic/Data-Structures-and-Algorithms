class Solution:

    def subArraySum(self,arr, tar):
        #Your code here

        cnt, curr_sum, d = 0, 0, {0:1}

        for num in arr:
            curr_sum += num

            if (curr_sum - tar) in d:
                cnt += d[curr_sum - tar]

            if curr_sum in d:
                d[curr_sum] += 1
            else:

                d[curr_sum] = 1
        return cnt