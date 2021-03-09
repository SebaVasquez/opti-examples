import matplotlib.pyplot as plt
import networkx as nx
from scipy.spatial import ConvexHull
from numpy import array

class Plotter:
    def __init__(self, instance):
        self.instance = instance
        self.graph = nx.Graph()
        self.pos = {node: node.pos for node in instance.nodes + [instance.node_to_verify]}
        self._load_base_data()

    def load_data(self, line_to_plot=None):
        nodes = self.instance.nodes + [self.instance.node_to_verify]
        fig, (ax1, ax2) = plt.subplots(ncols=2)

        color_map = ['black' for node in self.instance.nodes] + ['red']

        convex_hull = self._get_convex_hull()
        arcs = [(self.instance.nodes[i], self.instance.nodes[j]) for (i, j) in zip(convex_hull.vertices[:-1], convex_hull.vertices[1:])]\
                + [(self.instance.nodes[convex_hull.vertices[-1]], self.instance.nodes[convex_hull.vertices[0]])]
        self.graph.add_edges_from(arcs)

        nx.draw_networkx(self.graph, self.pos, edgelist=[], node_color=color_map, node_size=20, with_labels=False, ax=ax1)
        nx.draw_networkx(self.graph, self.pos, node_color=color_map, edge_color='gold', node_size=20, with_labels=False, ax=ax2)

        ax1.set_title('Node to verify: {}'.format(self.instance.node_to_verify.pos))

        if line_to_plot:
            epsilon = 1e-1
            alpha, beta = line_to_plot
            nodes = self.instance.nodes + [self.instance.node_to_verify]

            # axlim_x = array(ax1.get_xlim())
            # axlim_y = array(ax1.get_ylim())

            xlim = array([min([node.pos[0] for node in nodes]), max([node.pos[0] for node in nodes])])
            ylim = (beta + epsilon) / alpha[1] - (alpha[0] / alpha[1]) * xlim

            ax2.set_title('Solution: Node does not belong to conv()')

            plt.plot(xlim, ylim)
        else:
            ax2.set_title('Solution: Node belongs to conv()')

    def _load_base_data(self):
        nodes = self.instance.nodes + [self.instance.node_to_verify]
        for node in nodes:
            self.graph.add_node(node)
            self.graph.nodes[node]['pos'] = node.pos
    
    def _get_convex_hull(self):
        convex_hull = ConvexHull([node.pos for node in self.instance.nodes])
        return convex_hull

    def plot(self):
        mng = plt.get_current_fig_manager()
        mng.resize(*mng.window.maxsize())
        plt.show()