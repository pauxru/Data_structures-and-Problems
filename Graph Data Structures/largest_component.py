
components = ({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
})  # -> 4

components1 = ({
  3: [],
  4: [6],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1]
})  # -> 5


def largest_component(graph):
    bigger = 0
    visited = set()

    for node in graph:
        curr_size = explore_graph(graph, node, visited)
        if curr_size > bigger:
            bigger = curr_size

    return bigger


def explore_graph(graph, current, visited):
    if current in visited:
        return 0
    visited.add(current)

    size = 1
    for neighbor in graph[current]:
        ''' 
        For every neighbor increment 
        size by 1
        '''
        size += explore_graph(graph, neighbor, visited)

    return size


print(largest_component(components))
