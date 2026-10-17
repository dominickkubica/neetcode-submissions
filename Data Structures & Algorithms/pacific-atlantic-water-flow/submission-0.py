class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic_cells = set()
        pacific_cells = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        rows, cols = len(heights), len(heights[0])

        for r in range(rows):
            pacific_cells.add((r,0)) ### left side, pacifc..?
            atlantic_cells.add((r, cols - 1))### right side, atlantic..        
        for c in range(cols):
            pacific_cells.add((0,c)) ######## pacific top 
            atlantic_cells.add((rows - 1,c)) #### Atlantic bottom
            

        def bfs(ocean):
            q = deque(ocean)
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc 
                    if (0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[row][col] and (nr,nc) not in ocean):
                        q.append((nr,nc))
                        ocean.add((nr,nc))

        bfs(atlantic_cells)
        bfs(pacific_cells)
        answer = []
        for cell in  pacific_cells & atlantic_cells:
            answer.append(list(cell))
        return answer