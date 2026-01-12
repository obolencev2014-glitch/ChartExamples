import matplotlib.pyplot as plt
import numpy as np

def plot_chart():
    x = np.arange(0, 2 * np.pi, 0.01)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)

    ax.set(
        xlabel="x",
        ylabel="sin(x)",
        title="График синуса matplotlib"
    )
    ax.grid()

    plt.show()
