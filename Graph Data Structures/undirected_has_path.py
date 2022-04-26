from collections import deque

# Consider the non-directional graph below
graph1 = {'i': ['j', 'k'], 'j': ['i'], 'k': ['i', 'm', 'l'], 'm': ['k'], 'l': ['k'], 'o': ['n'], 'n': ['o']}


def has_path_dfs(graph, start, end):
    stack = deque(graph[start])
    visited = set()

    while len(stack) > 0:
        current = stack.pop()

        if current == end:
            print(f"Nodes {start} <--> {end}")
            return True

        if current in visited:
            continue
        visited.add(current)

        for neighbor in graph[current]:
            stack.append(neighbor)
    print(f"Nodes {start} -x- {end}")
    return False


has_path_dfs(graph1, 'i', 'o')
