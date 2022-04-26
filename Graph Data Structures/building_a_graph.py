
edges = [['i', 'j'], ['k', 'i'], ['m', 'k'], ['k', 'l'], ['o', 'n']]


def build_graph(nodes):
    """
    The function makes an adjacency list
    which in python is a dict. Key value pairing
    :param nodes: A list of lists
    :return: dictionary data type
    """
    graph = {}
    for node in nodes:
        [key, value] = node
        if key not in graph:
            graph[key] = []
        if value not in graph:
            graph[value] = []
        graph[key].append(value)
        graph[value].append(key)
    return graph


print(build_graph(edges))
