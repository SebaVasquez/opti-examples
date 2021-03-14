from argparse import ArgumentParser
import matplotlib.pyplot as plt
import os, sys
sys.path.append(os.getcwd())

from src.non_linear_problems.linear_regression.classes.instance import Instance
from src.non_linear_problems.linear_regression.model.model import RegressionModel
from src.non_linear_problems.linear_regression.plotter.plotter import Plotter

def run(factors, obs):

    instance = Instance(factors, obs)
    model = RegressionModel(instance)
    plotter = Plotter()
    m, n = model.solve()
    print('\nbeta_0: {} -- beta_1: {}'.format(n, m))

    if factors == 1:
        plotter.plot(instance, line=(m[0], n))
    else:
        plotter.plot(instance)

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        '-f', '--factors', 
        type=int,
        help='Number of factors')
    parser.add_argument(
        '-o', '--observations', 
        type=int,
        help='Number of observations')
    args = parser.parse_args()

    obs = args.observations or 200
    factors = args.factors or 3

    run(factors, obs)