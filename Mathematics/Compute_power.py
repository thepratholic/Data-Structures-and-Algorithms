def power(x, n):
    if n == 0:
        return 1
    tmp = power(x, n // 2)
    tmp *= tmp
    if n % 2 == 0:
        return tmp
    else:
        return tmp * x

# Test the function
print(power(5, 2))
