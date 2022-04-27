# Consider the non-directional graph below
graph1 = {'i': ['j', 'k'], 'j': ['i'], 'k': ['i', 'm', 'l'], 'm': ['k'], 'l': ['k'], 'o': ['n'], 'n': ['o']}
components = ({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
})  # -> 2

components1 = ({
  3: [],
  4: [6],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1]
})  # -> 3


def count_connected_components(graph):
    count = 0
    visited = set()

    for node in graph:
        if explore_graph(graph, node, visited) is True:
            count += 1

    return count


def explore_graph(graph, current, visited):
    if current in visited:
        return False
    visited.add(current)

    for neighbor in graph[current]:
        explore_graph(graph, neighbor, visited)

    return True


print(count_connected_components(components1))
