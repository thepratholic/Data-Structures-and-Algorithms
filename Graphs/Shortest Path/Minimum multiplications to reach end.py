from collections import deque

class Solution:
    def minimumMultiplications(self, arr, start, end):
        q = deque()
        MOD = 100000

        if start == end:
            return 0

        q.append((start, 0)) # node, minimum steps

        distance = [float("inf")] * 100000

        distance[start] = 0

        while q:
            node, current_steps = q.popleft()

            if node == end:
                return current_steps

            for i in range(len(arr)):

                num = (arr[i] * node) % MOD

                if current_steps + 1 < distance[num]:
                    distance[num] = current_steps + 1
                    q.append((num, current_steps + 1))

        return -1