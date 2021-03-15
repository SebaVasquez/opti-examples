from argparse import ArgumentParser
import os, sys
sys.path.append(os.getcwd())

from src.graph_problems.convex_hull_exclusion.classes.instance import Instance
from src.graph_problems.convex_hull_exclusion.solver import Solver
from src.graph_problems.convex_hull_exclusion.plotter.plotter import Plotter

def run(nodes, dimension, seed):
    instance = Instance(nodes, dimension, seed)
    print('Using nodes: {}\nand node to verify: {}\n'.format([x.pos for x in instance.nodes], instance.node_to_verify.pos))
    solver = Solver(instance)
    inclusion, plane = solver.solve()

    plotter = Plotter(instance)
    plotter.load_data(line_to_plot=plane)
    plotter.plot()


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        '-k', 
        type=int,
        help='Number of nodes')
    parser.add_argument(
        '-n', 
        type=str,
        help='Dimension of node position vector')
    parser.add_argument(
        '-s', '--seed', 
        type=int,
        help='Random seed to generate instance')
    args = parser.parse_args()

    nodes = args.k or 6
    dimension = args.n or 2
    seed = args.seed or 0

    run(nodes, dimension, seed)