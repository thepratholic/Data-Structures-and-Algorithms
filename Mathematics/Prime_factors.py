def primeFactors(n):
    if n <= 1:
        return

    i = 2
    while i * i <= n:
        while n % i == 0:
            print(i, end=" ")
            n //= i
        i += 1

    if n > 1:
        print(n, end=" ")

# Test the function
primeFactors(12)
