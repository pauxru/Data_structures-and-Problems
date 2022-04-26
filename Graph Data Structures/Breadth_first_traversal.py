from collections import deque

# Consider the directional graph below
graph1 = {'a': ['b', 'c'], 'b': ['d'], 'c': ['e'], 'd': ['f'], 'e': [], 'f': []}


def breadth_first_traversal(graph, start_point):
    queue = deque([start_point])

    while len(queue) > 0:
        current = queue.pop()  # A - B - C -> current
        print(current)

        for neighbor in graph[current]:
            queue.appendleft(neighbor)  # neighbor -> A - B - C


breadth_first_traversal(graph1, 'a')  # a-b-c-d-e-f
