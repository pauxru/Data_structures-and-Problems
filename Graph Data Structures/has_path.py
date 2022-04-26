from collections import deque

# Consider the directional graph below
graph1 = {'a': ['b', 'c'], 'b': ['d'], 'c': ['e'], 'd': ['f'], 'e': [], 'f': []}


# Depth first traversal
def has_path_dft(graph, start, end):
    stack = deque(graph[start])

    while len(stack) > 0:
        current = stack.pop()
        print(current)

        if current == end:
            print("Path Found")
            return True

        for neighbor in graph[current]:
            stack.append(neighbor)
    print("No path found")
    return False


has_path_dft(graph1, 'a', 'e')


# Breadth first search
def has_path_bfs(graph, start, end):
    queue = deque(graph[start])

    while len(queue) > 0:
        current = queue.pop()
        print(current)

        if current == end:
            print("Path Found")
            return True

        for neighbor in graph[current]:
            queue.appendleft(neighbor)
    print("No path found")
    return False


has_path_bfs(graph1, 'a', 'e')
