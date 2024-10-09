def sumExists(arr, N, sum):
    #Your code here
    s = set()
    new = set(arr)
    for i in new:
        if sum - i in s:
            return 1
        else:
            s.add(i)
    return 0

print(sumExists([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 14))