import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('tkAgg')
from argparse import ArgumentParser
import os, sys
sys.path.append(os.getcwd())

from src.graph_problems.classes.instance import GraphInstance
from src.graph_problems.classes.solution import GraphSolution
from src.graph_problems.tsp.model.model import TSPModel
from src.graph_problems.tsp.plotter.plotter import Plotter

def run(n, dist='uniform', metric='euclidean', seed=0):
    # Instance generation
    instance = GraphInstance('-'.join([str(n), dist, metric]), n, seed=seed)
    instance.dist = dist
    instance.metric = metric
    instance.generate_instance()

    # Model generation
    model = TSPModel(instance)

    # Solving
    model.solve()
    solution = GraphSolution(model.vars)

    # Plotting instance and solution
    plotter = Plotter(instance)
    plotter.load_data(solution.route_arcs)
    plotter.plot()

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        '-n', '--nodes', 
        type=int,
        help='Number of nodes')
    parser.add_argument(
        '-m', '--metric', 
        type=str,
        help='Metric to use when calculating arcs weigth')
    parser.add_argument(
        '-s', '--seed', 
        type=int,
        help='Random seed to generate instance')
    args = parser.parse_args()

    nodes = args.nodes or 10
    metric = args.metric or 'euclidean'
    seed = args.seed or 0

    run(nodes, metric=metric, seed=seed)