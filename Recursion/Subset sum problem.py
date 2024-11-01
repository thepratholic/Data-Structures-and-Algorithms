def subsets(arr, n, sum):
    if n == 0:
        return 1 if sum == 0 else 0
    return subsets(arr, n-1, sum) + subsets(arr, n-1, sum - arr[n-1])

print(subsets([10, 15, 20], 3, 25))