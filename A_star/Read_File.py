def read(name):
    graph = {}
    heuristic_value = {}
    file = open(name, 'r')
    for it in file:
        node = it.split()
        for i in range(0, len(node), 2):
            if i == 0:
                heuristic_value.update({node[i]: int(node[i + 1])})
                graph.update({node[0]: []})
            else:
                graph[node[0]].append({node[i]: int(node[i + 1])})
    return graph, heuristic_value
