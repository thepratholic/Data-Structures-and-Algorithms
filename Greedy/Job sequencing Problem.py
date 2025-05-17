class Solution:
    def JobScheduling(self, jobs):
        #your code goes here
        jobs.sort(key=lambda x:x[2], reverse=True)
        n = len(jobs)

        hash = [-1] * n
        cnt, totalProfit = 0, 0
        for i in range(n):

            for j in range(jobs[i][1] - 1, -1, -1):
                if hash[j] == -1:
                    cnt += 1
                    hash[j] = jobs[i][0]
                    totalProfit += jobs[i][2]
                    break
        
        return [cnt, totalProfit]
