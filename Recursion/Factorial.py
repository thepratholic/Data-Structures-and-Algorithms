def solve(n):
    if n < 1:
        return -1
    
    if n == 1:
        return 1
    
    return n * solve(n - 1)



if __name__ == "__main__":
    n = 4
    print(solve(n))