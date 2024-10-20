from typing import List


class Solution:
    def stringSequence(self, target: str) -> List[str]:
        result = []
        current = ""
        for char in target:
            current += 'a'
            result.append(current)
            presses = (ord(char) - ord('a')) % 26

            for _ in range(presses):
                current = current[:-1] + chr((ord(current[-1]) - ord('a') + 1) % 26 + ord('a'))
                result.append(current)

        return result