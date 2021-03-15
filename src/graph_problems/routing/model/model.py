from gurobipy import Model, GRB, quicksum
from itertools import combinations

class RoutingModel:
    def __init__(self, instance):
        self.instance = instance
        self._problem = None
        self.model = Model()
        self.vars = dict()
        self._outgoing_arcs = {
            i: [a for a in instance.costs.keys() if a[0] == i] for i in instance.nodes
        }
        self._incoming_arcs = {
            i: [a for a in instance.costs.keys() if a[1] == i] for i in instance.nodes
        }
    
    @property
    def problem(self):
        return self._problem
    
    @problem.setter
    def problem(self, problem):
        problems_dict = {
            'tsp': TSPModel(self.instance),
            'vrp': VRPModel(self.instance),
        }
        self._problem = problems_dict.get(problem)

    def _get_power_set(self, nodes):
        for t in range(2, len(nodes)):
            for S in combinations(nodes, t):
                yield S
    
    def _get_arcs_within_set(self, subset):
        for i, j in self.instance.costs.keys():
            if i in subset and j in subset:
                yield i, j

    def solve(self):
        self._problem.solve()
        return self._problem.vars
    

class TSPModel(RoutingModel):
    def __init__(self, instance):
        super().__init__(instance)
        self._set_model(instance)
        
    def _set_model(self, instance):
        nodes = instance.nodes
        costs = instance.costs
        arcs = costs.keys()
        model = self.model

        x = model.addVars(arcs, vtype=GRB.BINARY)

        model.addConstrs(quicksum(x[a] for a in self._outgoing_arcs[i]) == 1 for i in nodes)
        model.addConstrs(quicksum(x[a] for a in self._incoming_arcs[i]) == 1 for i in nodes)

        model.addConstrs(quicksum(x[a] for a in self._get_arcs_within_set(S)) <= len(S) - 1 for S in self._get_power_set(nodes))

        obj_func = quicksum(costs[a] * x[a] for a in arcs)
        model.setObjective(obj_func, sense=GRB.MINIMIZE)

        self.vars['x'] = x
        
    def solve(self):
        self.model.optimize()

class VRPModel(RoutingModel):
    def __init__(self, instance):
        super().__init__(instance)
        self._set_model(instance)

    def _get_outgoing_arcs_from_S(self, S):
        return [a for a in self.instance.costs.keys() if a[0] in S]
    
    def _get_subsets_by_size(self, nodes, size):
        yield combinations(nodes, size)
        
    def _set_model(self, instance):
        nodes = set(instance.nodes)
        depot = instance.depot
        fleet = instance.fleet
        costs = instance.costs
        arcs = costs.keys()
        model = self.model

        min_nodes_per_route = (len(nodes) - 1) // fleet

        x = model.addVars(arcs, vtype=GRB.BINARY)

        model.addConstrs(quicksum(x[a] for a in self._outgoing_arcs[i]) == 1 for i in nodes - {depot})
        model.addConstrs(quicksum(x[a] for a in self._incoming_arcs[i]) == 1 for i in nodes - {depot})

        model.addConstr(quicksum(x[a] for a in self._outgoing_arcs[depot]) == fleet)
        model.addConstr(quicksum(x[a] for a in self._incoming_arcs[depot]) == fleet)

        model.addConstrs(quicksum(x[a] for a in self._get_arcs_within_set(S)) <= len(S) - 1 for S in self._get_power_set(nodes - {depot}))

        model.addConstrs(
            quicksum(x[a] for a in self._get_arcs_within_set(S + (depot, ))) <= len(S) 
            for size in range(1, min_nodes_per_route) for subsets in self._get_subsets_by_size(nodes - {depot}, size) for S in subsets
        )

        obj_func = quicksum(costs[a] * x[a] for a in arcs)
        model.setObjective(obj_func, sense=GRB.MINIMIZE)

        self.vars['x'] = x
        
    def solve(self):
        self.model.optimize()

