from collections import deque

# Consider the directional graph below
graph1 = {'a': ['b', 'c'], 'b': ['d'], 'c': ['e'], 'd': ['f'], 'e': [], 'f': []}


def depth_first_traversal(graph, start_point):
    stack = deque([start_point])

    while len(stack) > 0:
        current = stack.pop()  # A-B-C-> current
        print(current)

        for neighbor in graph[current]:
            stack.append(neighbor)  # A-B-C- <- neighbor


# depth_first_traversal(graph1, 'a')  # a-c-e-b-d-f


def depth_first_traversal_recursion(graph, start_point):
    stack = [start_point]
    while len(stack) > 0:
        current = stack.pop()
        print(current)

        for neighbor in graph[current]:
            depth_first_traversal_recursion(graph, neighbor)


depth_first_traversal_recursion(graph1, 'a')  # a-b-d-f-c-e
