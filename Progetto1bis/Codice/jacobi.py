import numpy as np


def jacobi(it):
    return it.x + (it.residuoNum() / it.matA.diagonal())
