"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited = {node: Node(node.val)}
        q = deque([node])

        while q:
            room = q.popleft()
            for door in room.neighbors:
                if door not in visited:
                    visited[door] = Node(door.val) 
                    q.append(door)
                visited[room].neighbors.append(visited[door])
        return visited[node]