from classes.instance import Instance
from classes.solution import Solution
from model.model import TSP
from plotter.plotter import Plotter

import matplotlib.pyplot as plt

def run(n, dist='uniform', metric='euclidean', seed=0):
    # Instance generation
    instance = Instance('-'.join([str(n), dist, metric]), n, seed=seed)
    instance.dist = dist
    instance.metric = metric
    instance.generate_instance()

    # Model generation
    model = TSP(instance)

    # Solving
    model.solve()
    solution = Solution(model.vars)

    # Plotting instance and solution
    plotter = Plotter(instance)
    
    plotter.load_data()
    plt.show(block=False)
    plotter.load_data(solution.route_arcs)
    plt.show()

if __name__ == '__main__':
    run(13, seed=1)

