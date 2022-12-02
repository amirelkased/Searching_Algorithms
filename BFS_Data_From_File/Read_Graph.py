def fileName(name):
    file = open(name, 'r')
    graph_represent = {}
    for it in file:
        line = it.split()
        first_node = line.pop(0)
        graph_represent.update({first_node: line})
    return graph_represent
