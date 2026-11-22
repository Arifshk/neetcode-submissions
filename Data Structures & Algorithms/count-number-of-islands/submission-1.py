class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()
        count = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            if r >= rows or r<0 or c >= cols or c<0:
                return
            if grid[r][c] == "0":
                return 
            if (r,c) in visited:
                return 
            visited.add((r,c))
            for dr, dc in directions: 
                nr, nc = r + dr, c + dc
                dfs(nr, nc)
    
        for r in range (rows):
            for c in range (cols):
                if grid[r][c] != "0" and (r,c) not in visited:
                    count += 1
                    dfs(r,c)

                        
        return count


                  



                    
      