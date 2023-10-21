"""Module that optimizes data using Ford Fulkers method."""
import numpy as np
import pandas as pd

df = np.array(
    pd.read_csv('aboba.csv')[
        ['start', 'end', 'quantity_limit']
    ],
)

max_ = df.max() + 1

grh = [[0] * max_ for _ in range(max_)]

for vertex in df:
    start, end, capacity = vertex
    grh[start][end] = capacity
    grh[end][start] = capacity


class Solve:
    def __init__(self, graph: list[list[int | float]]) -> None:
        self.graph = graph
        self.ROW = len(graph)

    def bfs(self, source: int, target: int, parent: list[int]) -> bool:
        visited = [False] * (self.ROW)
        queue = []
        queue.append(source)
        visited[source] = True
        while queue:
            next = queue.pop(0)
            for ind, capacity in enumerate(self.graph[next]):
                if visited[ind] is False and capacity > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = next
                    if ind == target:
                        return True
        return False

    def ford_fulkerson(self, source: int, sink: int) -> int | float:
        parent = [-1] * (self.ROW)
        max_flow = 0
        while self.bfs(source, sink, parent):
            path_flow = float('inf')
            fst = sink
            while fst != source:
                path_flow = min(path_flow, self.graph[parent[fst]][fst])
                fst = parent[fst]

            max_flow += path_flow

            snd = sink
            while snd != source:
                u = parent[snd]
                self.graph[u][snd] -= path_flow
                self.graph[snd][u] += path_flow
                snd = parent[snd]
        return max_flow

print(Solve(grh).ford_fulkerson(1, 22))
