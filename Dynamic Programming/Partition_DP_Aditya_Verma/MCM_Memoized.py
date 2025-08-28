# matrix chain multiplication memoized code

def solve(nums, i, j, dp):
    if i >= j:
        return 0
    
    if dp[i][j] != -1:
        return dp[i][j]
    
    mini = float('inf')
    for k in range(i, j):
        temp = nums[i - 1] * nums[k] * nums[j] + solve(nums, i, k, dp) + solve(nums, k + 1, j, dp)

        mini = min(mini, temp)

    dp[i][j] = mini
    return dp[i][j]

def main():
    nums = [1, 2, 3, 4]
    n = len(nums)
    dp = [[-1] * n for _ in range(n)]
    print(solve(nums, 1, 3, dp))

if __name__ == "__main__":
    main()

# Output is : 18