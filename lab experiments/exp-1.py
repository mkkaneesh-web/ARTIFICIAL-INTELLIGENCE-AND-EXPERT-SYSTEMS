from collections import deque
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

queue = deque([('A', ['A'])])
visited = set()

while queue:
    room, path = queue.popleft()

    if room == 'F':
        print("Shortest path:", path)
        break

    if room not in visited:
        visited.add(room)

        for next_room in graph[room]:
            queue.append((next_room, path + [next_room]))
