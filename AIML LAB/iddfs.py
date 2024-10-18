from collections import deque

def iddfs(graph, start, goal):
   
    for depth in range(1, len(graph) + 1):
        result = dls(graph, start, goal, depth)
        if result is not None:
            return result
    return None

def dls(graph, start, goal, depth):
   
    stack = deque([(start, [start])])
    while stack:
        node, path = stack.pop()
        if node == goal:
            return path
        if len(path) < depth:
            for neighbor in graph[node]:
                stack.append((neighbor, path + [neighbor]))
    return None

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
goal_node = 'F'

result = iddfs(graph, start_node, goal_node)
if result is not None:
    print("Path found:", " -> ".join(result))
else:
    print("No path found")