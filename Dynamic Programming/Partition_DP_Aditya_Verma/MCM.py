# matrix chain multiplication 

def solve(nums, i, j):
    if i >= j:
        return 0
    
    mini = float('inf')
    for k in range(i, j):
        temp = nums[i - 1] * nums[k] * nums[j] + solve(nums, i, k) + solve(nums, k + 1, j)

        mini = min(mini, temp)

    return mini


def main():
    nums = [1, 2, 3, 4]
    print(solve(nums, 1, 3))

if __name__ == "__main__":
    main()

# output is : 18