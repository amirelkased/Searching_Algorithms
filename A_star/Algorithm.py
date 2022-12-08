# Designed By: Amir Elkased

opened = []
closed = []


def A(graph, heuristic, init, goal):
    opened.append({init: heuristic[init]})
    while True:
        node = get_next_node()
        node_char = list(node)
        closed.append(node)
        if node_char[0] == goal:
            return closed
        for iterator in graph[node_char[0]]:
            curr_node_char = list(iterator)[0]
            if not check(curr_node_char):
                iterator[curr_node_char] = iterator[curr_node_char] + node[node_char[0]] \
                                           - heuristic[node_char[0]] + heuristic[curr_node_char]
                opened.append(iterator)


def get_next_node():
    mini = 100
    idx = -1
    i = 0
    for x in opened:
        char = list(x)[0]
        if x[char] < mini:
            mini = x[char]
            idx = i
        i += 1
    return opened.pop(idx)


def check(dit):
    for i in opened:
        if list(i)[0] == dit:
            return True
    return False
