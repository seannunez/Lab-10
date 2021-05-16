import matplotlib.pyplot as plt
import numpy as np

A = np.array([[2, 0], [0, 1]])
B = np.array([[3, 0], [0, 1]])
C = np.identity(2)


def plotquiv(a, b):
    A = a @ b
    size = (10, 10)
    plt.figure(figsize=(4, 4))
    plt.xlim(-size[0], size[0])
    plt.ylim(-size[1], size[1])
    plt.xticks(np.arange((-size[0]), size[0] + 1, 1.0))
    plt.yticks(np.arange((-size[1]), size[1] + 1, 1.0))
    plt.scatter(A[0, :], A[1, :], label="APoints", color="Magenta")
    plt.title("Laboratory 10 - Linear Transformations")
    plt.grid()
    plt.show()


plotquiv(A, C)
plotquiv(A, B)
