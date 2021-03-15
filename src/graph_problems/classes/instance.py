import numpy as np
from itertools import permutations

from src.graph_problems.classes.node import Node

class GraphInstance:
    def __init__(self, id, n, fleet=1, seed=0):
        self.id = str(id)
        self.n = n
        self.seed = np.random.seed(seed)
        self.nodes = list()
        self.depot = None
        self.costs = dict()
        self.fleet = fleet

    def __str__(self):
        return self.id

    @property
    def dist(self):
        return self._dist
    
    @property
    def metric(self):
        return self._metric

    @dist.setter
    def dist(self, new_dist):
        dist_dict = {
            'uniform': np.random.randint,
            'normal': np.random.standard_normal
        }
        self._dist = dist_dict.get(new_dist, 'uniform')

    @metric.setter
    def metric(self, new_metric):
        metric_dict = {
            'euclidean': self._get_euclidean_costs,
            'manhattan': self._get_manhattan_costs
        }
        self._metric = metric_dict.get(new_metric, 'euclidean')
    
    def generate_instance(self, depot):
        self.nodes, self.costs = self._generate_data()
        self.depot = self.nodes[depot]

    def _generate_data(self):
        pos = self._dist(0, 100, size=(self.n, 2))
        nodes = [Node(idx, p) for idx, p in enumerate(pos)]
        costs = self._get_arcs_costs(nodes)

        return nodes, costs
    
    def _get_arcs_costs(self, nodes, metric='euclidean'):
        return self._metric(nodes)
    
    def _get_euclidean_costs(self, nodes):
        costs = {
            (i, j): np.linalg.norm(i.pos - j.pos) for i, j in permutations(nodes, 2)
        }
        return costs
    
    def _get_manhattan_costs(self, nodes):
        costs = {
            (i, j): np.linalg.norm(i.pos - j.pos, 1) for i, j in permutations(nodes, 2)
        }
        return costs