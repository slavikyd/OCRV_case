import numpy as np
import pandas as pd

df = np.array(
    pd.read_csv('hackathon_sirius_data.csv')[
        ['start', 'end', 'quantity_limit']
    ],
)

graph = {}
visited = {}

for vertex in df:
    start, end, capacity = vertex
    visited[start] = False
    visited[end] = False
    if start not in graph:
        graph[start] = {end: capacity}
    else:
        graph[start][end] = capacity


def reset_visited():
    for key in visited.keys():
        visited[key] = False


def mse(y, y_pred):
    return (y - y_pred) ** 2


def grad(v, last_value):
    visited[v] = True
    for ind, val in graph[v].items():
        if not visited[ind]:
            loss = mse(last_value, val)
            if last_value is not None and loss > 0:
                graph[v][ind] -= 1
            grad(ind, val)


num_epochs = 5000

start_vertext = df[0]

for _ in range(1, num_epochs + 1):
    grad(start_vertext[0], start_vertext[-1])
    reset_visited()

print(graph)
