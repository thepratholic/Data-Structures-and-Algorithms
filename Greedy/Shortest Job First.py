class Solution:
    def solve(self, bt):
        #your code goes here
        n = len(bt)
        bt.sort()
        total_time = 0
        wait_time = 0

        for i in range(n):
            wait_time += total_time
            total_time += bt[i]

        return wait_time // n 