from gurobipy import Model, quicksum, GRB

class IandPModel:
    def __init__(self, instance):
        self.model = Model()
        self.vars = dict()
        self._set_model(instance)
    
    def _set_model(self, instance):
        T = instance.periods
        c = instance.c
        h = instance.h
        d = instance.d
        model = self.model

        x = model.addVars(range(T))
        z = model.addVars(range(T))

        model.addConstrs(z[t] == z[t - 1] + x[t] - d[t] for t in range(1, T))
        model.addConstr(z[0] == x[0] - d[0])

        obj = quicksum(c[t] * x[t] + h[t] * z[t] for t in range(T))
        model.setObjective(obj, sense=GRB.MINIMIZE)

        self.vars = {
            'x': x,
            'z': z
        }

    def solve(self):
        self.model.optimize()