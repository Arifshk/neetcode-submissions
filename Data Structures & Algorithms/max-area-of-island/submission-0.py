class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        best = 0
        seen = set()
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        rows, cols = len(grid), len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0 or (row,col)in seen:
                    continue 

                area = 0 
                seen.add((row,col))
                stack = [(row,col)]

                while stack:
                   r, c = stack.pop()
                   area += 1
                   for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols
                        and grid[nr][nc]== 1 
                        and (nr, nc) not in seen):
                        seen.add((nr, nc))
                        stack.append((nr, nc))
                    best = max(best, area)
        return best
        #setup a count for max
        # seen set()
        #setup directions for grid to follow
        #check connected islands, lone island also equals to 1 
        # max formula is max number of 1s tog in directions, not their index 
        # skip 0s and seen 1s
        # return the max
      


        