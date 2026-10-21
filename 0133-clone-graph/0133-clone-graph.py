class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node):
        if node is None:
            return None

        copies = {}  

        def dfs(original):
            if original in copies:       
                return copies[original]

            clone = Node(original.val)    
            copies[original] = clone      

            for nb in original.neighbors:
                clone.neighbors.append(dfs(nb))
            return clone

        return dfs(node)