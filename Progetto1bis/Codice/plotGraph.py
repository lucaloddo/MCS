import iterativeMethod as itM
import numpy as np
import matplotlib.pyplot as plt
import readMatrix as rd
import re

def plot(matrix, tol):
    print("TOLLERANZA")
    print(tol)
    methods = ["Jacobi", "GaussSeidel","Gradiente","GradienteConiugato"]
    matrix = rd.read(matrix)
    i=0
    plot_size = 4
    text_size = 2
    ax_pos = [[(0, 0), (4, 0)], [(0, 1), (4, 1)], [(6, 0), (10, 0)],[(6, 1), (10, 1)]]
    for method in methods:
        iterativeObj = itM.IterativeMethod(matrix, tol)
        iterativeObj.solve(method)
        print(iterativeObj.errore)
        print(np.arange(iterativeObj.nIterations))

        ax_plot = plt.subplot2grid((12, 2), ax_pos[i][0], rowspan=4, colspan=1)
        ax_text = plt.subplot2grid((12, 2), ax_pos[i][1], rowspan=2, colspan=1)
        ax_plot.plot(np.arange(iterativeObj.nIterations), iterativeObj.errore)
        testo="Number of iterations: "+str(iterativeObj.nIterations)+"\nElapsed time: "+str(iterativeObj.time)
        ax_text.text(0.2, 0.2, testo,fontsize=10)
        ax_text.set_xticks([])
        ax_text.set_yticks([])
        ax_plot.set_ylabel("error")
        ax_plot.set_title(str(method))
        i=i+1

    plt.subplots_adjust (hspace=1)
    plt.show()
    return plt

