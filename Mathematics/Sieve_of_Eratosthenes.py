def sieve(n):
    v = [True] * (n + 1)

    for i in range(2, n + 1):
        if v[i]:
            for j in range(2 * i, n + 1, i):
                v[j] = False

    for i in range(2, n + 1):
        if v[i]:
            print(i, end=" ")

# Test the function
sieve(10)
