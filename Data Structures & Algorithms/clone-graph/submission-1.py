"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        visited = {node: Node(node.val)}
        q = deque([node])


        while q:
            room = q.popleft()
            for nxt in room.neighbors:
                if nxt not in visited:
                    visited[nxt] = Node(nxt.val)
                    q.append(nxt)

                visited[room].neighbors.append(visited[nxt])
        return visited[node]