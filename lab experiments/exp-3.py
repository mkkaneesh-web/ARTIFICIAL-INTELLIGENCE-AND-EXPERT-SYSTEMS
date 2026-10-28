import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2)],
    'C': [('D', 1)],
    'D': []
}

queue = [(0, 'A', ['A'])]

while queue:
    cost, node, path = heapq.heappop(queue)

    if node == 'D':
        print("Path:", path)
        print("Cost:", cost)
        break

    for next_node, weight in graph[node]:
        heapq.heappush(queue, (cost + weight, next_node, path + [next_node]))
