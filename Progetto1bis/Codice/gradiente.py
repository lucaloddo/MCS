import numpy as np


def gradiente(it):
    residuo = it.residuoNum()
    y = it.matA.dot(residuo)
    transpose = residuo.transpose()
    a = transpose.dot(residuo)
    b = transpose.dot(y)
    alfa = np.divide(a, b)
    alfa_residuo = it.x + alfa * residuo
    return alfa_residuo