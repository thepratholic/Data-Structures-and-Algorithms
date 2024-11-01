def jos(n, k):
    if n == 1:
        return 0
    return (jos(n-1, k) + k) % k
print(jos(4, 2))