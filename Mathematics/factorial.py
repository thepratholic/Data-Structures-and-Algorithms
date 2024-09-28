def fact(n):
    if n <= 1:
        return n
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

# Test the function
print(fact(4))
