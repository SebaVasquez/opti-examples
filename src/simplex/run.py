from argparse import ArgumentParser
from time import time
import importlib
import os, sys
sys.path.append(os.getcwd())

from src.simplex.classes.instance import SimplexInstance as Instance
from src.simplex.classes.simplex import Simplex

def run():
    parser = ArgumentParser()
    parser.add_argument(
        '-i', '--instance', 
        type=str,
        help='Instance data obtained from ./src/simplex/constants.py')
    
    args = parser.parse_args()
    import_path = 'src.simplex.constants' 
    data = getattr(importlib.import_module(import_path), args.instance or 'consts_1')
    print('Solving LP with the following data:', data)

    # Algorithm's execution
    t0 = time()
    instance = Instance(data)
    simplex = Simplex(instance)
    iters, optimal = simplex.run()
    print('\n\nFinished after {} iterations. Time elapsed: {} secs.'.format(iters, round(time() - t0, 2)))
    if optimal:
        print('Optimal solution(s) found.')
    else:
        print('Optimal solution not found.')

if __name__ == '__main__':
    run()
