def isPower(n):
    return n & (n-1) == 0

print(isPower(4))