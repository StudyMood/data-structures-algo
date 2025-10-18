# This is DFS (Depth First Search).py
graph = {
    "A": ["B", "C"],
    "B": ["A", "C"],
    "C": ["A", "B"]
}


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

dfs(graph, "A")

