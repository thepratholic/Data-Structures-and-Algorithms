def isPalin(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1

    return True

def solve(s, i, j, dp):
    if i >= j:
        return 0
    
    if isPalin(s, i, j):
        return 0
    
    if dp[i][j] != -1:
        return dp[i][j]
    
    mini = float('inf')
    for k in range(i, j):
        temp = 1 + solve(s, i, k, dp) + solve(s, k + 1, j, dp)
        mini = min(mini, temp)

    dp[i][j] = mini
    return dp[i][j]


def main():
    s = "nitin"
    n = len(s)
    dp = [[-1] * n for _ in range(n)]
    print(solve(s, 0, n - 1, dp))

if __name__ == "__main__":
    main()