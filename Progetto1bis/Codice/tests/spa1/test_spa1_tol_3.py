import os
import unittest

import readMatrix
from iterativeMethod import IterativeMethod


class Spa1Tol3(unittest.TestCase):
    def setUp(self):
        path = os.getcwd()
        matrix = readMatrix.read(path + "/dati/spa1.mtx")
        tol = 10 ** -8
        self.it = IterativeMethod(matrix, tol)

    def testJacobi(self):
        self.it.solve("Jacobi")
        self.assertEqual(self.it.nIterations, 247)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 0.4)

    def testGaussSeidel(self):
        self.it.solve("GaussSeidel")
        self.assertEqual(self.it.nIterations, 24)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 10)

    def testGradiente(self):
        self.it.solve("Gradiente")
        self.assertEqual(self.it.nIterations, 8233)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 12)

    def testGradienteConiugato(self):
        self.it.solve("GradienteConiugato")
        self.assertEqual(self.it.nIterations, 177)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 0.5)
