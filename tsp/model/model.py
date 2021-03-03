from gurobipy import Model, GRB, quicksum
from itertools import combinations

class TSP:
    def __init__(self, instance):
        self.instance = instance
        self.model = Model()
        self.vars = dict()
        self._outgoing_arcs = {
            i: [a for a in instance.costs.keys() if a[0] == i] for i in instance.nodes
        }
        self._incoming_arcs = {
            i: [a for a in instance.costs.keys() if a[1] == i] for i in instance.nodes
        }
        self._set_model()
        

    def _set_model(self):
        nodes = self.instance.nodes
        costs = self.instance.costs
        arcs = costs.keys()
        model = self.model

        x = model.addVars(arcs, vtype=GRB.BINARY)
        self.vars = x

        model.addConstrs(quicksum(x[a] for a in self._outgoing_arcs[i]) == 1 for i in nodes)
        model.addConstrs(quicksum(x[a] for a in self._incoming_arcs[i]) == 1 for i in nodes)

        model.addConstrs(quicksum(x[a] for a in self._get_arcs_within_set(S, arcs)) <= len(S) - 1 for S in self._get_power_set(nodes))

        obj_func = quicksum(costs[a] * x[a] for a in arcs)
        model.setObjective(obj_func, sense=GRB.MINIMIZE)
        
    
    def solve(self):
        self.model.optimize()

    def _get_power_set(self, nodes):
        for t in range(2, len(nodes)):
            for S in combinations(nodes, t):
                yield S
    
    def _get_arcs_within_set(self, subset, arcs):
        for i, j in arcs:
            if i in subset and j in subset:
                yield i, j

