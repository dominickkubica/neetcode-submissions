class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        max_area = 0
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            that_island_size = 1
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    
                    if(0 <= nr < rows 
                        and 0 <= nc < cols 
                        and grid[nr][nc] == 1 
                        and (nr,nc) not in visited):
                        visited.add((nr,nc))
                        q.append((nr,nc))
                        that_island_size +=1
            return that_island_size
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    that_island_size = bfs(r,c)
                    max_area = max(max_area, that_island_size)
        return max_area