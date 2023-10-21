"""Module for visualize data."""
import matplotlib.pyplot as plt
import pandas as pd
import networkx as nx


def visualize(start_indexes: list, end_indexes: list, new_weights: list) -> None:
    """ Displays the graph on the screen
    
        Args:
            start_indexes: list of indexes
            end_indexes: list of ending indexes
            new_weights: list of new_weights for lines
    """
    graph = nx.DiGraph()
    for index in range(len(start_indexes)):
        graph.add_edge(
            start_indexes[index], end_indexes[index], weight=new_weights[index])
    pos = nx.spring_layout(graph, seed=50)
    nx.draw_networkx(graph, pos)
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels)
    plt.show()


dataframe = pd.read_csv('aboba.csv')

start_arr = dataframe['start'].to_list()
end_arr = dataframe['end'].to_list()
quantity_arr = dataframe['quantity_limit'].to_list()

visualize(a=start_arr, b=end_arr, new_weights=quantity_arr)