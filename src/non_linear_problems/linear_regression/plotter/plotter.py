import matplotlib.pyplot as plt

class Plotter:
    def plot(self, instance, line=None):
        if line:
            plt.scatter(instance.X, instance.Y)
            m, n = line
            x = instance.X
            y = m * instance.X + n
            plt.plot(x, y, color='red')
            plt.title('beta_0: {} -- beta_1: {}'.format(round(n, 2), round(m, 2)))
        else:
            fig, axes = plt.subplots(1, instance.factors)
            for i in range(instance.factors):
                ax = axes[i]
                if not i:
                    ax.set_ylabel('Y')
                ax.scatter(instance.X[:, i], instance.Y)
                ax.set_xlabel('X{}'.format(i + 1))

        plt.show()