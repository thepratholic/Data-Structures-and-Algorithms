def maxPieces(n, a, b, c):
    if n == 0: return 0

    if n <= -1:
        return -1

    res = max(maxPieces(n-a, a, b, c), maxPieces(n-b, a, b, c), maxPieces(n-c, a, b, c))

    if res == -1:
        return -1
    return res + 1

print(maxPieces(17, 10, 11, 3))