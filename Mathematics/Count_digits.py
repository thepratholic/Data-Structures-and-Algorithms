def countDigits(x):
    res = 0
    while x > 0:
        x //= 10
        res += 1
    return res

# Test the function
print(countDigits(784))
