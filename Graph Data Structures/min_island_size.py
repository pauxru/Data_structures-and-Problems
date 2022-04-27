
grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]  # -> 2


def island_size(graph):
    smallest = float('inf')  # positive infinity
    visited = set()

    for r in range(len(graph)):
        for c in range(len(graph[0])):
            current_size = explore_island(graph, r, c, visited)
            if current_size < smallest and current_size != 0:
                smallest = current_size
    return smallest


def explore_island(graph, r, c, visited):
    row_inbounds = 0 <= r < len(graph)
    col_inbounds = 0 <= c < len(graph[0])
    pos = str(r) + ',' + str(c)  # 4,6
    if not row_inbounds or not col_inbounds or graph[r][c] == 'W' or pos in visited:
        return 0
    visited.add(pos)
    size = 1
    size += explore_island(graph, r - 1, c, visited)  # Up
    size += explore_island(graph, r + 1, c, visited)  # down
    size += explore_island(graph, r, c - 1, visited)  # left
    size += explore_island(graph, r, c + 1, visited)  # right
    return size


print(island_size(grid))
