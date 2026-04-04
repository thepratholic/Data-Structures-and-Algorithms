from collections import deque

class Solution:
    def wordLadderLength(self, startWord, targetWord, wordList):
        q = deque()
        st = set(wordList)

        q.append((startWord, 1))
        st.discard(startWord)

        if startWord == targetWord:
            return 0

        while q:
            current_word, steps = q.popleft()

            if current_word == targetWord:
                return steps

            for i in range(len(current_word)):
                original = current_word[i]

                for ch in range(ord("a"), ord("z") + 1):
                    current_word = current_word[:i] + chr(ch) + current_word[i+1:]

                    if current_word in st:
                        st.discard(current_word)
                        q.append((current_word, steps + 1))

                current_word = current_word[:i] + original + current_word[i+1:]

        return 0