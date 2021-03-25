import matplotlib.pyplot as plt
from numpy import arange

class Plotter:
    def plot(self, instance, x, z):
        T = instance.periods
        c = instance.c
        h = instance.h
        d = instance.d

        fig, (ax1, ax2) = plt.subplots(ncols=2)
        ax1.set_title('Costs')
        ax2.set_title('Solution')

        width = 0.35
        ax1.bar(arange(1, T + 1) - width / 2, c, width, label='Production cost (c)')
        ax1.bar(arange(1, T + 1) + width / 2, h, width, label='Inventory cost (h)')
        ax1.set_xticks(arange(1, T + 1))
        ax1.legend()

        ax2.plot(range(1, T + 1), d, label='Demand (d)')
        ax2.plot(range(1, T + 1), x, label='Production (x)')
        ax2.plot(range(1, T + 1), z, label='Inventory (z)')
        ax2.set_xticks(arange(1, T + 1))
        ax2.legend()

        plt.show()