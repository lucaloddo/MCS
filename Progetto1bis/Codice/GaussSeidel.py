import numpy as np
from scipy.sparse.linalg import spsolve


def gaussSeidel(it):
    return it.x + spsolve(it.tril, it.residuoNum())