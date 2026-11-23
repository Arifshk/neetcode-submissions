"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

        1. visited set in main function
        2. dfs node 
        3. Base case , not node, if it is already, match the visited and clone it 
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def dfs(node):
            if not node:
                return None
            if node in visited:
                return visited[node]
            
            new_node = Node(node.val)
            visited[node] = new_node
            
            for n in node.neighbors:
                new_node.neighbors.append(dfs(n))
            return new_node

        return dfs(node) if node else None


          


                
                
                


        
        