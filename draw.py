import numpy as np
import matplotlib.pyplot as plt


def draw(x_arr, y_arr, func):
    plt.grid(True)
    plt.plot([x for x in x_arr], [y for y in y_arr], marker="o", label='y ~ f(x)')
    draw_interval(min(x_arr), max(x_arr), func)
    plt.xlabel('x')
    plt.ylabel('y', rotation=0)
    plt.legend()
    plt.show()


def draw_interval(a, b, func):
    X = np.arange(a, b, 1e-3)
    y = []
    for x in X:
        try:
            y.append(func.f_real(x))
        except ValueError:
            y.append(None)
    plt.plot(X, y, 'k', label="y = f(x)")
