from gurobipy import Model, quicksum, GRB

import numpy as np

class RegressionModel:
    def __init__(self, instance):
        self.model = Model()
        self.vars = dict()
        self._set_model(instance)

    def _set_model(self, instance):
        model = self.model
        factors = range(instance.factors)
        obs = range(instance.obs)
        X = instance.X
        Y = instance.Y

        beta_0 = model.addVar(lb=-GRB.INFINITY)
        beta_1 = model.addVars(factors, lb=-GRB.INFINITY)

        error = quicksum((Y[i] - beta_0 - quicksum(beta_1[j] * X[i][j] for j in factors)) ** 2 for i in obs)

        model.setObjective(error, sense=GRB.MINIMIZE)

        self.vars['beta_0'] = beta_0
        self.vars['beta_1'] = beta_1

    def solve(self):
        self.model.optimize()
        m = list(map(lambda x: x.X, self.vars['beta_1'].values()))
        n = self.vars['beta_0'].X

        return m, n 