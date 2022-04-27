from collections import deque

graph1 = {'a': ['c', 'b'], 'c': ['a', 'b', 'd'], 'b': ['a', 'c', 'd'],
          'd': ['c', 'b', 'e'], 'e': ['d'], 'g': ['f'], 'f': ['g']}


def find_shortest_path(graph, node_a, node_b):
    """
    shortest path is better done with BFS
    :param graph: The graph where path is sought
    :param node_a: Starting node
    :param node_b: end node
    :return: shortest path
    """
    queue = deque([[node_a, 0]])
    visited = set()

    while len(queue) > 0:
        [current, distance] = queue.pop()
        # print(f"{current} - {distance}")
        if current == node_b:
            return distance

        if current in visited:
            continue
        visited.add(current)

        for neighbor in graph[current]:
            queue.appendleft([neighbor, distance + 1])

    return -1


print(find_shortest_path(graph1, 'a', 'e'))
