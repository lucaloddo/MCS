import numpy as np

def gradienteConiugato(it):
    y = it.matA.dot(it.d)
    dPerY = it.d.dot(y)
    alfa = np.divide(it.d.dot(it.residuoNum()), dPerY)
    it.x = it.x + np.dot(alfa, it.d)
    nuovoResiduo = it.residuoNum()
    w = it.matA.dot(nuovoResiduo)
    beta = it.d.dot(w) / dPerY
    it.d = nuovoResiduo - np.dot(beta, it.d)
    return it.x
