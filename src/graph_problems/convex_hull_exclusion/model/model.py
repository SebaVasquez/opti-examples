from gurobipy import Model, quicksum, GRB

class CHEModel:
    def __init__(self, instance):
        self.convex_combination_model = Model()
        self.plane_separation_model = Model()
        self.vars = dict()
        self._set_ccm_model(instance)
        self._set_sp_model(instance)

    def _set_ccm_model(self, instance):
        nodes = instance.nodes
        node_to_verify = instance.node_to_verify
        model = self.convex_combination_model

        l = model.addVars(range(instance.k))
        self.vars['l'] = l

        model.addConstrs(quicksum(nodes[i].pos[comp] * l[i] for i in range(instance.k)) == node_to_verify.pos[comp] for comp in range(instance.n))
        model.addConstr(quicksum(l[i] for i in range(instance.k)) == 1)

        model.setObjective(0, sense=GRB.MINIMIZE)
    
    def _set_sp_model(self, instance):
        nodes = instance.nodes
        node_to_verify = instance.node_to_verify
        model = self.plane_separation_model

        a = model.addMVar(instance.n, lb=-GRB.INFINITY)
        b = model.addMVar(1, lb=-GRB.INFINITY)
        epsilon = 10
        
        model.addConstrs(a @ node.pos <= b - epsilon for node in nodes)
        model.addConstr(a @ node_to_verify.pos >= b + epsilon)

        model.setObjective(0, sense=GRB.MAXIMIZE)

        self.vars['a'] = a
        self.vars['b'] = b

    def _ccm_solve(self):
        self.convex_combination_model.optimize()

    def _ps_solve(self):
        self.plane_separation_model.optimize()