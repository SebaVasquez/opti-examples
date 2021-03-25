import os, sys
sys.path.append(os.getcwd())
from argparse import ArgumentParser

from src.continuous_problems.production_and_inventory_problem.classes.instance import Instance
from src.continuous_problems.production_and_inventory_problem.model.model import IandPModel
from src.continuous_problems.production_and_inventory_problem.plotter.plotter import Plotter

def run(periods):
    instance = Instance(periods)
    model = IandPModel(instance)
    model.solve()
    print('')
    for t in range(instance.periods):
        print('Period {}:\n\tParameters:'.format(t + 1))
        print('\t\tc: {}, h: {}, d: {}'.format(instance.c[t], instance.h[t], instance.d[t]))
        print('\tSolution:')
        print('\t\tx:', model.vars['x'][t].X)
        print('\t\tz:', model.vars['z'][t].X)
        print('\tCost:\n\t\t', model.vars['x'][t].X * instance.c[t] + model.vars['z'][t].X * instance.h[t])
    print('Total cost:', model.model.objval)

    x = [model.vars['x'][t].X for t in range(instance.periods)]
    z = [model.vars['z'][t].X for t in range(instance.periods)]

    plotter = Plotter()
    plotter.plot(instance, x, z)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        '-T', '--periods', 
        type=int,
        help='Problem to solve')
    args = parser.parse_args()

    periods = args.periods or 20

    run(periods)