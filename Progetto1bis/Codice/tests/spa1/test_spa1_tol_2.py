import os
import unittest

import readMatrix
from iterativeMethod import IterativeMethod


class Spa1Tol2(unittest.TestCase):
    def setUp(self):
        path = os.getcwd()
        matrix = readMatrix.read(path + "/dati/spa1.mtx")
        tol = 10 ** -6
        self.it = IterativeMethod(matrix, tol)

    def testJacobi(self):
        self.it.solve("Jacobi")
        self.assertEqual(self.it.nIterations, 181)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 0.3)

    def testGaussSeidel(self):
        self.it.solve("GaussSeidel")
        self.assertEqual(self.it.nIterations, 17)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 6)

    def testGradiente(self):
        self.it.solve("Gradiente")
        self.assertEqual(self.it.nIterations, 3577)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 5)

    def testGradienteConiugato(self):
        self.it.solve("GradienteConiugato")
        self.assertEqual(self.it.nIterations, 134)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 0.3)
