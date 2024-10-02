#check if string is palindrome or not

def f(i, s):
    if i >= len(s) // 2: return True
    if s[i] != s[len(s) - i - 1]: return False
    return f(i+1, s)


if __name__ == "__main__":
    print(f(0, "madam"))