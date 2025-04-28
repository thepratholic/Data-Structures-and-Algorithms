def odds(arr):
    xors = 0
    res1, res2 = 0, 0

    for i in arr:
        xors = xors ^ i

    sn = xors & ~(xors - 1)

    for i in arr:
        if i & sn != 0:
            res1 ^= i
        else:
            res2 ^= i

    print(res1, res2)

if __name__ == "__main__":
    arr = [3, 4, 3, 4, 5, 4, 4, 6, 7, 7]
    odds(arr)