import numpy as np
from scipy.linalg import cholesky

class Instance:
    def __init__(self, factors, obs):
        self.factors = factors
        self.obs = obs
        self.Y, self.X = self._gen_observations()
        
    def _gen_observations(self):
        x = np.random.randint(0, 100, size=(self.obs, self.factors))
        sign = np.random.choice([-1, 1], size=self.factors)
        m = np.random.uniform(0.3, 0.5, size=(self.obs, self.factors)) * sign
        n = np.random.uniform(5, 10, size=(self.obs, self.factors))
        y = m * x + n

        return np.mean(y, axis=1), x

        