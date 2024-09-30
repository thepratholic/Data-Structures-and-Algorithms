# calculate the maximum sum of k consecutive elements in the array


def calSum(arr, k):
    curr = 0
    for i in range(k):
        curr += arr[i]

    res = curr
    for i in range(k, len(arr)):
        curr += arr[i] - arr[i-k]
        res = max(res, curr)
    return res

print(calSum([1, 8, 30, -5, 20, 7], 4))