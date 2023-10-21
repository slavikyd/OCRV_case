"""Module that minimizes data."""
import numpy as np
import pandas as pd

df = np.array(
    pd.read_csv('hackathon_sirius_data.csv')[
        ['start', 'end', 'quantity_limit'],
    ],
)

graph = {}
min_ = float('inf')

for vertex in df:
    start, end, capacity = vertex
    min_ = min(min_, capacity)
    if start not in graph:
        graph[start] = {end: capacity}
    else:
        graph[start][end] = capacity

for verts in graph.values():
    for key in verts.keys():
        verts[key] = min_
