#Reverse array using recursive approach

def f(i, arr, n):
    if i >= n//2:
        return
    
    arr[i], arr[n-i-1] = arr[n-i-1], arr[i]

    f(i+1, arr, n)

if __name__ == "__main__":
    arr = [3, 5, 8, 2, 11]
    f(0, arr, len(arr))

    print(arr) 