import matplotlib.pyplot as plt
import numpy as np

def plot_chart():
    mean = 0
    sigma = 1

    x = np.arange(-5, 5, 0.01)
    y = np.exp(-np.square((x - mean) / sigma) / 2) / (np.sqrt(2 * np.pi) * sigma)

    fig, ax = plt.subplots()
    ax.plot(x, y)

    ax.set(
        xlabel="x",
        ylabel="y",
        title="Нормальное распределение"
    )
    ax.grid()

    plt.show()
