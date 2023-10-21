import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd


def visualize(a, b, new_weights):
    graph = nx.DiGraph()
    for i in range(len(a)):
        graph.add_edge(a[i], b[i], weight=new_weights[i])
    pos = nx.spring_layout(graph, seed=50)
    nx.draw_networkx(graph, pos)
    edge_labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels)

    plt.show()


data = pd.read_csv('aboba.csv')

start_arr = data['start'].to_list()
end_arr = data['end'].to_list()
quantity_arr = data['quantity_limit'].to_list()

visualize(a=start_arr, b=end_arr, new_weights=quantity_arr)