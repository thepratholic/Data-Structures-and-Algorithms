class Solution:
    def findCity(self, n, m, edges, distanceThreshold):
        distance = [[float("inf")] * n for _ in range(n)]

        for u, v, wt in edges:
            distance[u][v] = wt
            distance[v][u] = wt


        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

        
        city_count = n
        city_no = -1

        for city in range(n):
            count = 0
            for adjCity in range(n):
                if city != adjCity and distance[city][adjCity] <= distanceThreshold:
                    count += 1

            if count < city_count:
                city_count = count
                city_no = city

            elif count == city_count:
                city_no = city

        return city_no