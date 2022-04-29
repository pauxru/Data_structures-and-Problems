"""
The problem was sourced from:
https://www.youtube.com/watch?v=4tYoVx0QoN0&ab_channel=Cl%C3%A9mentMihailescu

Remove any island (1) which is not attached to the end of the land
end is defined: (r == 0 or r == len(graph) - 1) or (c == 0 or c == len(graph[0]) - 1)
"""

graph1 = [
     [1, 0, 0, 0, 0, 0],
     [0, 1, 0, 1, 1, 1],
     [0, 0, 1, 0, 1, 0],
     [1, 1, 0, 0, 1, 0],
     [1, 0, 1, 1, 0, 0],
     [1, 0, 0, 0, 0, 1]]

answer = [[1, 0, 0, 0, 0, 0],
          [0, 0, 0, 1, 1, 1],
          [0, 0, 0, 0, 1, 0],
          [1, 1, 0, 0, 1, 0],
          [1, 0, 0, 0, 0, 0],
          [1, 0, 0, 0, 0, 1]]


def delete_islands(graph):
    """
    Traverse through the grid and when a land (1) in the end is encountered.
    We explore the graph at that point
    :param graph: The entire grid with islands
    :return: the mutated graph with
    """
    visited = set()
    safe = []
    for r in range(len(graph)):
        for c in range(len(graph[r])):
            if graph[r][c] == 1 and (r == 0 or r == len(graph) - 1) or (c == 0 or c == len(graph[0]) - 1):
                explore_graph(graph, r, c, visited, safe)

    for rr in range(len(graph)):
        for cc in range(len(graph[rr])):
            graph[rr][cc] = 0
    for island in safe:
        [r, c] = island
        graph[r][c] = 1
    return graph


def explore_graph(graph, r, c, visited, safe):
    row_inbounds = 0 <= r < len(graph)
    col_inbounds = 0 <= c < len(graph[0])
    pos = str(r) + "," + str(c)  # 11,3

    if pos in visited or not row_inbounds or not col_inbounds:
        return False

    val_at_pos = graph[r][c]
    if val_at_pos == 0:
        return False
    else:
        safe.append([r, c])
    visited.add(pos)
    explore_graph(graph, r - 1, c, visited, safe)  # Up
    explore_graph(graph, r + 1, c, visited, safe)  # Down
    explore_graph(graph, r, c - 1, visited, safe)  # Right
    explore_graph(graph, r, c + 1, visited, safe)  # Left
    return True


print(graph1)
print(delete_islands(graph1))
