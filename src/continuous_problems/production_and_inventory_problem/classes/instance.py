import numpy as np
np.random.seed(0)

class Instance:
    def __init__(self, periods):
        self.periods = periods
        self.c = np.random.randint(1, 3, size=periods)
        self.h = np.random.randint(1, 4, size=periods)
        self.d = np.random.randint(50, 100, size=periods)