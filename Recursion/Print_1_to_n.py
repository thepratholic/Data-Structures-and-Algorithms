def solve(n):
    if n == 1:
        print(n, end=" ")
        return
    
    solve(n - 1)
    print(n, end= " ")


if __name__ == "__main__":
    n = 7
    solve(n)