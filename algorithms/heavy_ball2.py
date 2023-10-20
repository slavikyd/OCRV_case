import heapq

# Функция для поиска кратчайшего пути с помощью алгоритма тяжёлого шарика
def heavy_ball(graph, source, target):
    n = len(graph)
    distances = [float('inf')] * n
    distances[source] = 0

# Создаем очередь с приоритетами и добавляем начальную вершину
    pq = [(0, source)]

    while pq:
        weight, node = heapq.heappop(pq)

# Если достигнута целевая вершина, возвращаем найденный путь
        if node == target:
            return distances[node]

# Перебираем соседние вершины текущей вершины
    for neighbor, edge_weight in graph[node].items():
        new_dist = distances[node] + edge_weight

# Если найден более короткий путь к соседней вершине, обновляем расстояние
    if new_dist < distances[neighbor]:
        distances[neighbor] = new_dist
        heapq.heappush(pq, (new_dist, neighbor))

# Если путь не найден, возвращаем None
    return None

# Пример использования алгоритма
graph = {
0: {1: 4, 2: 2},
1: {2: 1, 3: 5},
2: {3: 8},
3: {0: 3}
}
source = 0
target = 3

shortest_path = heavy_ball(graph, source, target)
print("Кратчайший путь с минимальной стоимостью:", shortest_path)