class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        ocean_a = set()
        ocean_b = set()

        def dfs(r, c, visited):
            visited.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visited)

        for c in range(cols):
            dfs(0, c, ocean_a)
            dfs(rows - 1, c, ocean_b)

        for r in range(rows):
            dfs(r, 0, ocean_a)
            dfs(r, cols - 1, ocean_b)

        return [[r, c] for r, c in ocean_a if (r, c) in ocean_b]