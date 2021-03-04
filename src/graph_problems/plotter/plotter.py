import matplotlib.pyplot as plt
import networkx as nx

class Plotter:
    def __init__(self, instance):
        self.instance = instance
        self.graph = nx.Graph()
        self.pos = {node: node.pos for node in instance.nodes}
        self._load_base_data()

    def load_data(self, arcs_to_plot=list()):
        self.graph.add_edges_from(arcs_to_plot)
        nx.draw(self.graph, self.pos)

    def _load_base_data(self):
        self.graph = nx.Graph()
        for node in self.instance.nodes:
            self.graph.add_node(node)
            self.graph.nodes[node]['pos'] = node.pos

    def plot():
        plt.plot()