from src.classes.solution import Solution

class GraphSolution(Solution):
    def __init__(self, vars):
        super().__init__(vars)
        self.route_arcs = self._get_route_arcs(vars)
    
    def _get_route_arcs(self, vars):
        return [a for a in vars if vars[a].X > .5]