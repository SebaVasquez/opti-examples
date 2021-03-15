import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('tkAgg')
from argparse import ArgumentParser
import os, sys
sys.path.append(os.getcwd())

from src.graph_problems.routing.classes.instance import Instance
from src.graph_problems.routing.classes.solution import Solution
from src.graph_problems.routing.model.model import RoutingModel
from src.graph_problems.routing.plotter.plotter import Plotter

def run(problem, n, metric, fleet, depot, seed, dist='uniform'):
    # Instance generation
    instance = Instance('-'.join([str(n), dist, metric]), n, fleet, seed)
    instance.dist = dist
    instance.metric = metric
    instance.generate_instance(depot)

    # Model generation
    model = RoutingModel(instance)
    model.problem = problem

    # Solving
    vars = model.solve()
    solution = Solution(vars)

    # Plotting instance and solution
    plotter = Plotter(instance)
    plotter.load_data(solution.route_arcs)
    plotter.plot()

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        '-p', '--problem', 
        type=str,
        help='Problem to solve')
    parser.add_argument(
        '-n', '--nodes', 
        type=int,
        help='Number of nodes')
    parser.add_argument(
        '-m', '--metric', 
        type=str,
        help='Metric to use when calculating arcs weigth')
    parser.add_argument(
        '-f', '--fleet', 
        type=int,
        help='Fleet size')
    parser.add_argument(
        '-d', '--depot', 
        type=int,
        help='Depot node index')
    parser.add_argument(
        '-s', '--seed', 
        type=int,
        help='Random seed to generate instance')
    args = parser.parse_args()

    problem = args.problem or 'vrp'
    nodes = args.nodes or 12
    metric = args.metric or 'euclidean'
    fleet = args.fleet or 1
    depot = args.depot or 0
    seed = args.seed or 0

    run(problem, nodes, metric, fleet, depot, seed)