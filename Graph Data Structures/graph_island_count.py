

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]  # -> 3

grid1 = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]  # -> 4


def island_count(graph):
    visited = set()
    count = 0

    for r in range(len(graph)):
        for c in range(len(graph[0])):
            if explore_island(graph, r, c, visited) is True:
                count += 1
    return count


def explore_island(graph, r, c, visited):
    row_inbounds = 0 <= r < len(graph)
    col_inbounds = 0 <= c < len(graph[0])
    pos = str(r) + ',' + str(c)
    if not row_inbounds or not col_inbounds or graph[r][c] == "W" or pos in visited:
        return False
    visited.add(pos)

    explore_island(graph, r - 1, c, visited)  # up
    explore_island(graph, r + 1, c, visited)  # down
    explore_island(graph, r, c - 1, visited)  # left
    explore_island(graph, r, c + 1, visited)  # right
    return True


print(island_count(grid1))
