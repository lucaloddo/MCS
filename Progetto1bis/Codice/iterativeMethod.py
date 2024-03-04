import logging
import time

import numpy as np
from scipy.sparse import tril

from GaussSeidel import gaussSeidel
from gradiente import gradiente
from gradienteConiugato import gradienteConiugato
from jacobi import jacobi


class IterativeMethod:
    def __init__(self, matA, tol):
        self.matA = matA
        self.exactX = np.ones(matA.shape[0])
        self.x = np.zeros(matA.shape[0])
        self.b = matA.dot(self.exactX)
        self.tol = tol
        self.time = time.time()
        self.nIterations = 0
        self.maxIter = 20000
        self.d = self.residuoNum()
        self.tril=tril(self.matA).tocsr()
        self.errore=[]
        self.denominator=np.linalg.norm(self.b)

    def residuoNum(self):
        return np.subtract(self.b, self.matA.dot(self.x))

    def stopIter(self):
        numerator = np.linalg.norm(self.residuoNum())

        if (numerator / self.denominator) < self.tol:
            return False
        else:
            return True

    def solve(self, nomeMetodo):
        while self.stopIter():

            self.x = self.update(nomeMetodo)
            self.errore.append(self.relativeError())
            self.nIterations += 1
            if self.nIterations > self.maxIter:
                logging.info("Max number of iterations reached: method failed to converge")
                break
        end = time.time()
        self.time = end - self.time
        logging.info("Number of iterations: " + str(self.nIterations))
        logging.info("Relative error: " + str(self.percentageError()))
        logging.info("Percentage error: " + str(round(self.percentageError(), 2)) + "%")
        logging.info("Elapsed time: " + str(round(self.time, 2)) + " seconds")

    def update(self, nomeMetodo):
        if nomeMetodo == "Jacobi":
            return jacobi(self)
        elif nomeMetodo == "GaussSeidel":
            return gaussSeidel(self)
        elif nomeMetodo == "Gradiente":
            return gradiente(self)
        elif nomeMetodo == "GradienteConiugato":
            return gradienteConiugato(self)

    def absoluteError(self):
        return np.linalg.norm(np.subtract(self.x, self.exactX))

    def relativeError(self):
        return np.divide(self.absoluteError(), np.linalg.norm(self.x))
    def percentageError(self):
        return self.relativeError() * 100