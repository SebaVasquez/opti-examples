import numpy as np

from src.graph_problems.classes.instance import GraphInstance
from src.graph_problems.classes.node import Node

class Instance(GraphInstance):
    def __init__(self, k, n, seed):
        super().__init__(None, n, seed)
        self.k = k
        self.node_to_verify = None
        self._generate_nodes()

    def _generate_nodes(self):
        pos_array = np.random.normal(0, 1, size=(self.k, self.n)) * 1000
        for idx, pos in enumerate(pos_array):
            node = Node('x{}'.format(idx), pos)
            self.nodes.append(node)
        self.node_to_verify = Node('x', np.random.normal(0, 1, size=self.n) * 1000)
