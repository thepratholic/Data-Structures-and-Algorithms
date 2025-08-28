def isPalin(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1

    return True

def solve(s, i, j):
    if i >= j:
        return 0
    
    if isPalin(s, i, j):
        return 0
    
    mini = float('inf')
    for k in range(i, j):
        temp = 1 + solve(s, i, k) + solve(s, k + 1, j)
        mini = min(mini, temp)

    return mini


def main():
    s = "nitin"
    print(solve(s, 0, 4))

if __name__ == "__main__":
    main()