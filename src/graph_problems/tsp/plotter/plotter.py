import matplotlib.pyplot as plt
import networkx as nx

class Plotter:
    def __init__(self, instance):
        self.instance = instance
        self.graph = nx.Graph()
        self.pos = {node: node.pos for node in instance.nodes}
        self._load_base_data()

    def load_data(self, arcs_to_plot=list()):
        fig, (ax1, ax2) = plt.subplots(ncols=2)
        ax1.set_title('Instance')
        ax2.set_title('Solution')

        nx.draw(self.graph, self.pos, ax=ax1)
        self.graph.add_edges_from(arcs_to_plot)
        nx.draw(self.graph, self.pos, ax=ax2)

    def _load_base_data(self):
        for node in self.instance.nodes:
            self.graph.add_node(node)
            self.graph.nodes[node]['pos'] = node.pos

    def plot(self):
        mng = plt.get_current_fig_manager()
        mng.resize(*mng.window.maxsize())
        plt.show()