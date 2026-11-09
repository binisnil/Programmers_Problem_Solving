from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    dist = [[-1] * m for _ in range(n)]
    dist[0][0] = 1
    queue = deque([(0, 0)])
        
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if dist[nr][nc] == -1 and maps[nr][nc] == 1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
    return dist[n-1][m-1]