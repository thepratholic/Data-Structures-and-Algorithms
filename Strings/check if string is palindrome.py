def isPalin(s):
    if s == s[::-1]: return True
    else: return False

print(isPalin("ABBA"))