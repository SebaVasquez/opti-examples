from src.graph_problems.convex_hull_exclusion.model.model import CHEModel
from numpy import array

class Solver:
    def __init__(self, instance):
        self.node_to_verify = instance.node_to_verify
        self.model = CHEModel(instance)

    def solve(self):
        plane = None
        feasibility = True
        self.model._ccm_solve()
        if self.model.convex_combination_model.status == 2:
            print('\nPoint x is within the convex hull')
        else:
            print('\nPoint x is not within the convex hull.\nComputing the separator plane...')
            self.model._ps_solve()
            alpha = self.model.vars['a'].X
            beta = self.model.vars['b'].X
            plane = (alpha, beta)
            feasibility = False
            print('A feasible pair of parameters is:\nalpha = {} -- beta = {}'.format(alpha, beta))
        
        return feasibility, plane

