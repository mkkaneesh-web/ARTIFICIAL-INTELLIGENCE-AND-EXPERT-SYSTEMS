import heapq

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

h = {'A': 5, 'B': 3, 'C': 2, 'D': 0}

queue = [(h['A'], 'A')]
visited = set()
parent = {}

while queue:
    _, city = heapq.heappop(queue)

    if city in visited:
        continue

    visited.add(city)

    if city == 'D':
        break

    for next_city in graph[city]:
        if next_city not in visited:
            parent[next_city] = city
            heapq.heappush(queue, (h[next_city], next_city))

path = []
city = 'D'

while city in parent:
    path.append(city)
    city = parent[city]

path.append('A')
path.reverse()

print("Path:", path)
