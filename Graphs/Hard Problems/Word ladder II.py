from collections import deque

class Solution:
    def findSequences(self, beginWord, endWord, wordList):
        st = set(wordList)
        q = deque()
        q.append([beginWord])
        st.discard(beginWord)
        ans = []
        toErase = set()

        while q:
            size = len(q)

            for _ in range(size):
                current_seq = q.popleft()

                word = current_seq[-1]
                if word == endWord:
                    if not ans:
                        ans.append(current_seq)

                    elif len(current_seq) == len(ans[-1]):
                        ans.append(current_seq)


                for pos in range(len(word)):
                    original = word[pos]

                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        word = word[:pos] + ch + word[pos + 1:]

                        if word in st:
                            current_seq.append(word)

                            q.append(list(current_seq))
                            toErase.add(word)
                            current_seq.pop()

                    word = word[:pos] + original + word[pos + 1:]

            for it in toErase:
                st.discard(it)

            toErase.clear()

            if ans:
                break

        return ans

