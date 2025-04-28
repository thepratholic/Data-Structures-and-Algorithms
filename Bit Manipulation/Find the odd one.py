def odds(arr):
    res = 0
    for x in arr:
        res ^= x

    print(res)

odds([10, 10, 40, 50, 50])