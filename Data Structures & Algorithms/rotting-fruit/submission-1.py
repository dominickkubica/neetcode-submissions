class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        oranges = 0
        rows, cols = len(grid), len(grid[0])
        minutes = 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    oranges +=1
                elif grid[r][c] == 2:
                    q.append((r,c))

        while q and oranges > 0:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if(0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1):
                        q.append((nr,nc))
                        grid[nr][nc] = 2
                        oranges -=1 
            minutes +=1
        return minutes if oranges == 0 else -1