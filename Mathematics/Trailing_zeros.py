def trailed(n):
    num_of_zeros = 0
    while n % 10 == 0:
        num_of_zeros += 1
        n //= 10
    return num_of_zeros

# Test the function
print(trailed(1000))
