import os
import unittest

import readMatrix
from iterativeMethod import IterativeMethod


class Vem2Tol2(unittest.TestCase):
    def setUp(self):
        path = os.getcwd()
        matrix = readMatrix.read(path + "/dati/vem2.mtx")
        tol = 10 ** -6
        self.it = IterativeMethod(matrix, tol)

    def testJacobi(self):
        self.it.solve("Jacobi")
        self.assertEqual(self.it.nIterations, 3676)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 1)

    def testGaussSeidel(self):
        self.it.solve("GaussSeidel")
        self.assertEqual(self.it.nIterations, 1840)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 18)

    def testGradiente(self):
        self.it.solve("Gradiente")
        self.assertEqual(self.it.nIterations, 2438)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 1)

    def testGradienteConiugato(self):
        self.it.solve("GradienteConiugato")
        self.assertEqual(self.it.nIterations, 56)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 1)
