"""Module for visualize data."""
import networkx as nx
from matplotlib import pyplot as plt

from ford_fulkerson import visualizer

graph = nx.DiGraph()
for vertex in visualizer():
    graph.add_edge(vertex[0], vertex[1], weight=vertex[2])

pos = nx.spring_layout(graph, seed=50)
nx.draw_networkx(graph, pos)

edge_labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels)
plt.show()
