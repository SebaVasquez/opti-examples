
class GraphSolution:
    def __init__(self, vars):
        self.vars = vars
        self.route_arcs = self._get_route_arcs(vars)
    
    def _get_route_arcs(self, vars):
        return [a for a in vars if vars[a].X > .5]