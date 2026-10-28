
import heapq

def greedy_best_first_search(graph, heuristic, start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], start))

    visited = set()
    parent = {}

    while priority_queue:
        h, current = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)
        print("Visiting:", current)

        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            return path

        for neighbor in graph[current]:
            if neighbor not in visited:
                parent[neighbor] = current
                heapq.heappush(
                    priority_queue,
                    (heuristic[neighbor], neighbor)
                )

    return None


# Warehouse locations and connecting paths
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

# Estimated distance from each location to the goal
heuristic = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 3,
    'E': 2,
    'F': 1,
    'G': 0
}

start = 'A'
goal = 'G'

path = greedy_best_first_search(graph, heuristic, start, goal)

if path:
    print("Path found:", " -> ".join(path))
else:
    print("No path found")
