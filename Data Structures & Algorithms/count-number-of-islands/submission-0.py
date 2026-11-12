class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        total = 0 
        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        rows, cols = len(grid), len(grid[0])
        for row in range (rows):
            for col in range (cols):
                if grid[row][col]!= "1" or (row,col) in visited:
                    continue
                total += 1
                visited.add((row,col))
                stack = [(row, col)]
                while stack:
                    r, c = stack.pop()
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (0 <= nr < rows and 0 <= nc < cols
                                and grid[nr][nc] == "1"
                                and (nr,nc) not in visited):
                            visited.add((nr,nc))
                            stack.append((nr,nc))
        return total