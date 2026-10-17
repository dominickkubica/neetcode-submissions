from collections import deque   
class Solution: 
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]

        def bfs(r,c):
            q = deque([(r,c)])
            visited.add((r,c))            
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < rows 
                        and 0 <= nc < cols 
                        and grid[nr][nc] == '1' 
                        and (nr,nc) not in visited):
                        q.append((nr,nc))
                        visited.add((nr,nc))                        
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c)
                    islands+=1
        return islands