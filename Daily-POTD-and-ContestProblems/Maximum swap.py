class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = str(num)
        n = len(num_str)
        maxi = num
        for i in range(n):
            for j in range(i+1, n):
                num_list = list(num_str)
                num_list[i], num_list[j] = num_list[j], num_list[i]

                tmp = int("".join(num_list))

                maxi = max(maxi, tmp)
        return maxi