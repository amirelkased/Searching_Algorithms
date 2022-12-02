queue = []
visited = []


def bfs(Graph, init_state):
    visited.append(init_state)
    queue.append(init_state)
    while queue:
        node = queue.pop(0)
        for neighbours in Graph.get(node):
            if neighbours not in visited:
                queue.append(neighbours)
                visited.append(neighbours)
    return visited