from collections import deque

def can_reach(grid, health):
    m, n = len(grid), len(grid[0])
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    queue = deque([(0, 0, health)])
    
    visited = set([(0, 0, health)])
    
    while queue:
        x, y, h = queue.popleft()
        
        if (x, y) == (m - 1, n - 1):
            if h >= 1:
                return True
            continue

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < m and 0 <= ny < n:
                new_health = h - 1 if grid[nx][ny] == 1 else h
                
                if new_health > 0 and (nx, ny, new_health) not in visited:
                    visited.add((nx, ny, new_health))
                    queue.append((nx, ny, new_health))
    
    return False


print(can_reach([[1,1,1,1]], 4))