def isPalindrome(n):
    rev = 0
    temp = n
    while temp != 0:
        ld = temp % 10
        rev = rev * 10 + ld
        temp //= 10
    return rev == n

# Test the function
print(isPalindrome(7885))
