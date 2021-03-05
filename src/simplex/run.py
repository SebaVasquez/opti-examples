from argparse import ArgumentParser
from time import time
import os, sys
sys.path.append(os.getcwd())

from src.simplex.constants import consts_1, consts_2
from src.simplex.classes.instance import SimplexInstance as Instance
from src.simplex.classes.simplex import Simplex

def run():
    t0 = time()
    instance = Instance(consts_1)
    simplex = Simplex(instance)
    iters, optimal = simplex.run()
    print('\n\nFinished after {} iterations. Time elapsed: {} secs.'.format(iters, round(time() - t0, 2)))
    if optimal:
        print('Optimal solution(s) found.')
    else:
        print('Non-optimal solution found.')

if __name__ == '__main__':
    run()
