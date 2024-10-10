class Solution:
    def leftMost(self, s):
        visited = [False] * 256
        res = -1
        for i in range(len(s)-1, -1, -1):
            if visited[ord(s[i])] == True:
                res = i
            else:
                visited[ord(s[i])] = True

        return res
    
s = Solution()
print(s.leftMost("abccb"))