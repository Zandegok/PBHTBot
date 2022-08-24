import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.savefig('d')


def makeplot(*args):
    match args:
        case 'points', xs, ys:
            x = [*map(float, xs[1:-1].split(','))]
            y = [*map(float, ys[1:-1].split(','))]
            fig, ax = plt.subplots()
            ax.plot(x, y)
            plt.savefig('d.png')
            return open('d.png', 'rb')


def makeplotByPoints(xs, ys):
    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.savefig('d.png')
    return open('d.png', 'rb')
