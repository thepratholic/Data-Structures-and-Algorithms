from collections import deque
class Solution:
    def areSentencesSimilar(self, s1, s2):
        deq1 = deque(s1.split())
        deq2 = deque(s2.split())

        while deq1 and deq2 and deq1[0] == deq2[0]:
            deq1.popleft()
            deq2.popleft()

        while deq1 and deq2 and deq1[-1] == deq2[-1]:
            deq1.pop()
            deq2.pop()

        return not deq1 or not deq2
    
s = Solution()
print(s.areSentencesSimilar("Hello Jane", "Hello my name is Jane"))